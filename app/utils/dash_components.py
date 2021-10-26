import os
from importlib import import_module
from types import (
    ModuleType,
    FunctionType,
)
from typing import Any
from flask import Flask
from dash import Dash

from configs.dash import (
    components,
    settings,
)
from app.utils.extractions import get_functions_list


def add_modules_components_factory(server: Flask) -> Any:
    f"""
    :param server: Flask.
    The function is served as a decorator method that adds components from defined src app (in that case, 
    from {components.COMPONENTS_CURRENT_DIR} folder) to a a Dash app object that based on the Flask server input.
    It reads the all modules from the current dir, searches in each module a relevant component method 
    (based on defined pattern) and activates the method on the app object.
    :return: A wrapper that activates the logic above.
    """

    def add_modules_components(foo: FunctionType) -> Any:
        def wrapper() -> Dash:
            # create ann app object
            app: Dash = foo(server)
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
                            f"{components.MAIN_DASH_METHOD_PREFIX}{filename_without_extension}"
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
    return add_modules_components
