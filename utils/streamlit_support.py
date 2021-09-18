import streamlit as st
from typing import Dict
from types import FunctionType
# local modules
from utils.decoders import (
    read_html,
    bin_to_base64,
    switch_words_in_text,
)
from simulation_configs.streamlit_website.settings import Sidebar


def set_image_in_html(
        html_path: str,
        image_path: str
) -> str:
    """
    :param html_path: str. The HTML path with a correct template of background style, must include an image template.
    :param image_path: str. The relevant image path.
    :return: str. The HTML with the decoded image.
    The HTML content must to contain the word "FILE_PATH", in order to site the image in the HTML template.
    Otherwise - the function will raise an error.
    """
    # HTML content
    html_text = read_html(html_path)
    try:
        assert html_text.count("FILE_PATH")
    except AssertionError:
        raise NotImplemented("HTML content must to contain the word 'FILE_PATH' for making the switch.")

    # decoded image
    image = bin_to_base64(image_path)
    # the decoded image inside of the HTML template
    html_with_image = switch_words_in_text(
        text=html_text,
        FILE_PATH=image
    )
    return html_with_image


def create_sidebar(buttons_to_modules: Dict[str, FunctionType]) -> Dict:
    """
    The function creates a streamlit sidebar with buttons, when every button actually activate another function.
    :param buttons_to_modules: dict. The key is the button's name, and the value is the function the will be activate.
    """
    for button, func in buttons_to_modules.items():
        assert not func.__code__.co_argcount, f"Button's modules should be with no arguments. The button '{button}' " \
                                              f"activate function with {func.__code__.co_argcount} arguments"
        if st.sidebar.button(button):
            func()
    return Sidebar.FUNCTION_RESPONSE
