import streamlit as st
from PIL import Image
# local modules
from simulation_configs.streamlit_website import settings
from utils.streamlit_support import set_image_in_html


def home_page_runner() -> None:
    """
    GUI simulation home page basic definitions.
    """
    st.set_page_config(
        page_title=settings.WebsiteConfig.BROWSER_WINDOW_NAME,
        page_icon=Image.open(settings.Images.SOLAR_BOARDS_PATH),
        initial_sidebar_state=settings.WebsiteConfig.SIDEBAR_BEGINNING_MODE
    )
    st.title(settings.HomePageTitles.TITLE)
    st.subheader(settings.HomePageTitles.SUBTITLE)

    st.sidebar.title(settings.Sidebar.TITLE)
    st.sidebar.subheader(settings.Sidebar.SUBTITLE)
    st.sidebar.title(settings.Sidebar.EMPTY_TITLE)

    st.markdown(
        set_image_in_html(
            html_path=settings.HTML.BACKGROUND_PATH,
            image_path=settings.Images.RAIN_FOREST_PATH
        ),
        unsafe_allow_html=True
    )


def home_page_blueprint() -> None:
    """
    GUI simulation home page function when there is a pressing on the home page button.
    """
    pass


