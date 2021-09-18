import base64
import streamlit as st


@st.cache(allow_output_mutation=True)
def bin_to_base64(path: str) -> str:
    """
    :param path: str. The file's path for decoding.
    :return: str. The file in base64 format.
    """
    with open(path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def read_html(path: str) -> str:
    """
    The function reads HTML file from the given path.
    :param path: str. File's path.
    :return: str. File's HTML content as a text.
    """
    with open(path, 'rb') as f:
        text = f.read()
    return text.decode()


def switch_words_in_text(text: str, **kwargs) -> str:
    """
    The function switches the relevant key arguments (if exists) by their values.
    :param text: str. The HTML file's path.
    :param kwargs: dict. Every argument will be switched by his value as the text.
    :return: str. The HTML as string, after all the exchanges.
    """
    try:
        assert isinstance(text, str)
    except AssertionError:
        raise TypeError("The text must be a str")

    for key, val in kwargs.items():
        try:
            assert isinstance(key, str) and isinstance(val, str)
        except AssertionError:
            raise TypeError("The switch must to be between two strings")
        text = text.replace(key, val)

    return text



