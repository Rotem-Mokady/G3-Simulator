import os
from importlib import import_module
from inspect import (
    getmembers,
    isfunction,
)
from types import (
    ModuleType,
    FunctionType,
)
from typing import (
    Union,
    List,
    Any,
)
import re
import numpy as np
from flask import Flask
from dash import Dash
# local modules
from configs.dash import (
    components,
    settings,
)
from configs.secrets.auth_constants import (
    LOGIN_MANAGER,
    UsersApp,
)
from configs.secrets.db_constants import (
    SQLiteDB,
    Users,
)


def get_functions_list(file_module: ModuleType) -> Union[List, None]:
    """
    :param file_module: An object of python file ('.py' extension).
    :return: List of functions that define in this module.
    """
    # type checker
    if not isinstance(file_module, ModuleType):
        raise TypeError(f"file_module must be a module, got '{type(file_module).__name__}' instead")
    # read the file as text
    with open(file_module.__file__) as file:
        text = file.read()
    if not text:
        return
    # extract any function's name from this file.
    # that extraction included sub-functions in any function or class in this file, and also functions that have been
    # written as a string, without actually define any method
    defined_functions_from_text = list(map(
        lambda foo: foo.replace("def", "").replace("(", "").strip(),
        re.findall(re.compile(r"def\s+\w+\s{0,}\("), text)
    ))
    if not defined_functions_from_text:
        return
    # get a list of any defined or imported function in this module
    any_method_in_module = [foo[0] for foo in getmembers(file_module) if isfunction(foo[1])]
    if not any_method_in_module:
        return
    # cross the two lists and get a list of only outer functions in this module
    functions_list = np.array(defined_functions_from_text)[
        np.in1d(defined_functions_from_text, any_method_in_module)
    ].tolist()
    if not functions_list:
        return
    return functions_list


def add_modules_components(foo: FunctionType) -> Any:
    f"""
    :param foo: A method that returns a Flask object.
    The function is served as a decorator method that adds components from defined src app (in that case, 
    from {components.COMPONENTS_CURRENT_DIR} folder) to a an app object (Flask).
    It reads the all python modules from the current dir, searches in each module a relevant component method 
    (based on defined pattern) and activates the method on the app object.
    :return: A wrapper that activates the logic above.
    """
    # create ann app object
    app: Union[Flask, Dash] = foo()

    def wrapper() -> Dash:
        """
        :return: The app object itself.
        """
        # run on the configured dir path
        for file in os.listdir(components.COMPONENTS_CURRENT_DIR):
            # filter only relevant python files
            if file.endswith(settings.PY_FILE_EXTENSION) and file not in components.IRRELEVANT_FILES:

                filename_without_extension = file[:file.index(settings.PY_FILE_EXTENSION)]
                # import the module itself
                try:
                    curr_module: ModuleType = import_module(
                        "{current_dir}.{filename}".format(
                            current_dir=".".join(components.COMPONENTS_CURRENT_DIR.split("//")),
                            filename=filename_without_extension
                        )
                    )
                except ModuleNotFoundError:
                    raise ImportError(f"Can not import {file} from {components.COMPONENTS_CURRENT_DIR}")
                # get the components method from the current module
                try:
                    curr_method: FunctionType = curr_module.__dict__[
                        f"{settings.MAIN_DASH_METHOD_PREFIX}{filename_without_extension}"
                    ]
                except KeyError:
                    raise ImportError(
                        "No components function in '{file}'. Methods list:\n{functions_list}".format(
                            file=file,
                            functions_list=', '.join(get_functions_list(curr_module))
                        )
                    )
                # activate the method on the app object
                curr_method(app)
        return app
    return wrapper


def create_users_table() -> None:
    """
    The function creates the permissions sql table for the authentication table.
    """
    Users.metadata.create_all(SQLiteDB.ENGINE)


@LOGIN_MANAGER.user_loader
def load_user(user_id):
    return UsersApp.query.get(int(user_id))
