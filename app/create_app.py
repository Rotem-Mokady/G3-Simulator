from dash import (
    Dash,
    html,
)
from configs.dash import (
    styles,
    titles,
    tags,
)
from app.utils import add_modules_components


@add_modules_components
def create_app() -> Dash:
    """
    :return: An app object with the basic design and the modules components from the modules folder (app\\modules).
    """
    app = Dash()
    app.title = titles.TAB_WINDOW_NAME
    app.layout = html.Div(style=styles.BACKGROUND_STYLE, children=tags.FINAL_LAYOUT)
    return app
