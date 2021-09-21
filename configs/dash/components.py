import os
import math
from configs.dash.settings import PROJECT_NAME

COMPONENTS_CURRENT_DIR = "app\\modules"
CURR_PATH = os.getcwd().split("\\")
CURR_FOLDERS_DISTANCE = len(CURR_PATH) - CURR_PATH.index(PROJECT_NAME)

with open("{src}\\.gitignore".format(
        src="\\".join([
            (2 if CURR_FOLDERS_DISTANCE > 1 else 1) * "." for _ in range(math.ceil(CURR_FOLDERS_DISTANCE/2))
        ])
    )
) as file:
    IRRELEVANT_FILES = file.read().split("\n")
