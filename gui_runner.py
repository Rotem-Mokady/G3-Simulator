from simulation_configs.streamlit_website.sidebar_buttons_config import BUTTON_NAME_TO_MODULE
from gui_modules.blueprints.home_page import home_page_runner
from utils.streamlit_support import create_sidebar
from gui_modules.blueprints.tdh_by_flow_page import tdh_by_flow_blueprint


def main() -> None:
    """
    GUI simulation main function
    """
    home_page_runner()
    create_sidebar(BUTTON_NAME_TO_MODULE)
    # tdh_by_flow_blueprint()


if __name__ == '__main__':
    main()


