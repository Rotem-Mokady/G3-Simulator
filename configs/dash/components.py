import os
from configs.dash.settings import PROJECT_NAME

COMPONENTS_CURRENT_DIR = "app\\modules"
CURR_PATH = os.getcwd().split("\\")
CURR_FOLDERS_DISTANCE = len(CURR_PATH) - CURR_PATH.index(PROJECT_NAME) - 1

with open("{src}.gitignore".format(src="".join(["..\\" for _ in range(CURR_FOLDERS_DISTANCE)]))) as file:
    IRRELEVANT_FILES = file.read().split("\n")
