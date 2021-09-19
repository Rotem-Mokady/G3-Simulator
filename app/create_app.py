from dash import (
    Dash,
    html,
)
from dash.dependencies import (
    Input,
    Output,
)
from configs.dash import (
    settings,
    styles,
    titles,
    childrens,
    dropdown,
    inputs,
)
from configs.operationals import modules_names


def create_app() -> Dash:
    app = Dash()
    app.title = titles.TAB_WINDOW_NAME
    app.layout = html.Div(style=styles.BACKGROUND_STYLE, children=childrens.HOME_PAGE)

    @app.callback(Output(component_id=inputs.TDHbyFlow.ID, component_property=settings.STYLE_PROPERTY),
                  [Input(component_id=dropdown.ID, component_property=dropdown.PROPERTY)])
    def callback_module(value: str):
        if value == modules_names.TDH_BY_FLOW:
            return styles.BUTTONS_STYLE
        else:
            return styles.HIDE_STYLE
    return app
