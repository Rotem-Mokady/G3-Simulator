from dash import (
    Dash,
    html,
)
from configs.dash import (
    styles,
    titles,
    tags,
)
from app.tdh_by_flow import components_tdh_by_flow


def create_app() -> Dash:
    app = Dash()
    app.title = titles.TAB_WINDOW_NAME
    app.layout = html.Div(style=styles.BACKGROUND_STYLE, children=tags.HOME_PAGE)
    components_tdh_by_flow(app)
    return app
