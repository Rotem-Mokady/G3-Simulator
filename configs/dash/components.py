COMPONENTS_CURRENT_DIR = "app//modules"
MAIN_DASH_METHOD_PREFIX = "components_"

with open(".gitignore") as file:
    IRRELEVANT_FILES = file.read().split("\n")
