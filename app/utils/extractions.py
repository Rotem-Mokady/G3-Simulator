import os

from inspect import (
    getmembers,
    isfunction,
)
from types import ModuleType
from typing import (
    Union,
    List,
    Tuple,
)

import re
import numpy as np


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


def create_table_extraction(path: str) -> Union[Tuple[str, List], None]:
    """
    :param path: str. The path of create table SQL query.
    :return: Tuple. Table name and columns list, None for query that does not create table.
    """
    if not os.path.exists(path):
        raise ValueError(f"Path '{path}' does not exist")
    with open(path) as f:
        sql = f.read()

    create_table_line = re.findall(re.compile(r"(?:create|CREATE)\s+(?:table|TABLE)\s+\w+\s+"), sql)
    if not create_table_line:
        return
    if len(create_table_line) > 1:
        raise TypeError(f"file '{path}' should include only one query, ({len(create_table_line)} given)")

    table_name = create_table_line[0].strip().split()[-1]
    table_params_beginning_index = len(create_table_line[0])
    return table_name, [
        re.search(re.compile(r"\s{0,}\w+\s"), row).group().strip()
        for row in sql[table_params_beginning_index:].split(",")
    ]
