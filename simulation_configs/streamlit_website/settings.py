class WebsiteConfig:
    BROWSER_WINDOW_NAME = "G3 Simulator"
    SIDEBAR_BEGINNING_MODE = "collapsed"


class HomePageTitles:
    TITLE = "G3 Simulator"
    SUBTITLE = "Dashboard that simulate the behavior of R.A.O machine"


class Sidebar:
    FUNCTION_RESPONSE = {"success": True}
    TITLE = "Simulator Modules"
    SUBTITLE = "Choose your physical module"
    EMPTY_TITLE = ""


class HTML:
    BACKGROUND_PATH = "simulation_configs\\streamlit_website\\html\\background.html"


class Images:
    SOLAR_BOARDS_PATH = "simulation_configs\\streamlit_website\\images\\solar-boards.png"
    RAIN_FOREST_PATH = "simulation_configs\\streamlit_website\\images\\rain-forest.png"


class Inputs:
    BAD_RESPONSE = False


class TDHbyFlow:
    PIPE_HEIGHT_INPUT_BUTTON_NAME = "Pipe Height (in meters)"
    PIPE_HEIGHT_INPUT_MIN_VALUE = 0
    PIPE_HEIGHT_INPUT_GOOD_MESSAGE = "Excellent! Chosen pipe height - {user_input}"
    PIPE_HEIGHT_INPUT_WRONG_MESSAGE = "Incorrect pipe height - {user_input}"

    PIPE_DIAMETER_INPUT_BUTTON_NAME = "Pipe Diameter (in millimeters)"
    PIPE_DIAMETER_INPUT_MIN_VALUE = 0
    PIPE_DIAMETER_INPUT_GOOD_MESSAGE = "Excellent! Chosen pipe diameter - {user_input}"
    PIPE_DIAMETER_INPUT_WRONG_MESSAGE = "Incorrect pipe diameter - {user_input}"






