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
from dash import Dash
# local modules
from configs.dash import components


def get_functions_list(file_module: ModuleType) -> Union[List, None]:
    with open(file_module.__file__) as file:
        text = file.read()
    defined_functions_from_text = np.array(list(map(
        lambda foo: foo.replace("def ", "").replace("(", ""),
        re.findall(r"def \w+\(", text)
    )))
    if not defined_functions_from_text:
        return
    any_method_in_module = [foo[0] for foo in getmembers(file_module) if isfunction(foo[1])]
    functions_list = defined_functions_from_text[np.in1d(defined_functions_from_text, any_method_in_module)].tolist()
    return functions_list


def add_modules_components(foo: FunctionType) -> Any:
    app = foo()

    def wrapper() -> Dash:
        for file in os.listdir(components.COMPONENTS_CURRENT_DIR):
            if file.endswith(components.PY_FILE_EXTENSION) and file not in components.IRRELEVANT_FILES:

                filename_without_extension = file[:file.index(components.PY_FILE_EXTENSION)]
                try:
                    curr_module = import_module(
                        "{current_dir}.{filename}".format(
                            current_dir=".".join(components.COMPONENTS_CURRENT_DIR.split("\\")),
                            filename=filename_without_extension
                        )
                    )
                except ModuleNotFoundError:
                    raise ImportError(f"Can not import {file} from {components.COMPONENTS_CURRENT_DIR}")

                try:
                    curr_method = curr_module.__dict__[f"components_{filename_without_extension}"]
                except KeyError:
                    raise ModuleNotFoundError(
                        "No components function in '{file}'. Methods list:\n{functions_list}".format(
                            file=file,
                            functions_list=', '.join(get_functions_list(curr_module))
                        )
                    )

                curr_method(app)
        return app
    return wrapper


