import os
from dash import (
    Dash,
    html,
)
from configs.dash import (
    styles,
    titles,
    tags,
    settings,
)
from app.utils import add_modules_components


@add_modules_components
def create_app() -> Dash:
    """
    Project's tests will run based on the configuration.
    :return: An app object with the basic design and the modules components from the modules folder (app\\modules).
    """
    if settings.RUN_TESTS:
        os.system(settings.TESTS_COMMAND_LINE)
    app = Dash()
    app.title = titles.TAB_WINDOW_NAME
    app.layout = html.Div(style=styles.BACKGROUND_STYLE, children=tags.FINAL_LAYOUT)
    return app
