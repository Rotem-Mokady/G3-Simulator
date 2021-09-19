from dash import (
    html,
    dcc,
)
from configs.dash import (
    titles,
    styles,
    dropdown,
    inputs,
)
from configs.calcs.defaults.physical_deafult_params import Pipe


TDH_BY_FLOW = [
    html.Div(
        id=inputs.TDHbyFlow.ID,
        children=[
            html.Br(),
            dcc.Input(
                autoComplete=inputs.TDHbyFlow.Pipe.AUTO_COMPLETE,
                inputMode=inputs.TDHbyFlow.Pipe.MODE,
                min=inputs.TDHbyFlow.Pipe.MIN,
                value=inputs.TDHbyFlow.Pipe.AUTO_COMPLETE,
                placeholder=inputs.TDHbyFlow.Pipe.NAME,
                type=inputs.TDHbyFlow.Pipe.TYPE,
                style=styles.BUTTONS_STYLE
            ),
            html.Br(),
            dcc.Input(
                autoComplete=inputs.TDHbyFlow.Diameter.AUTO_COMPLETE,
                inputMode=inputs.TDHbyFlow.Diameter.MODE,
                min=inputs.TDHbyFlow.Diameter.MIN,
                value=inputs.TDHbyFlow.Diameter.AUTO_COMPLETE,
                placeholder=inputs.TDHbyFlow.Diameter.NAME,
                type=inputs.TDHbyFlow.Diameter.TYPE,
                style=styles.BUTTONS_STYLE
            ),
            html.Br(),
            dcc.Dropdown(
                options=[{"label": pipe_type, "value": pipe_type} for pipe_type in Pipe.TYPES_TO_E.keys()],
                searchable=inputs.TDHbyFlow.PipeType.SEARCHABLE,
                placeholder=inputs.TDHbyFlow.PipeType.NAME,
                value=inputs.TDHbyFlow.PipeType.AUTO_COMPLETE,
                style=styles.TDH_BY_FLOW_DROPDOWN_STYLE
            )
        ]
    )
]


HOME_PAGE = [
    html.H1(children=titles.HOME_PAGE_TITLE, style=styles.HOME_PAGE_TITLE_STYLE),
    html.H2(children=titles.HOME_PAGE_SUBTITLE, style=styles.HOME_PAGE_SUBTITLE_STYLE),
    html.H3(children=titles.HOME_PAGE_INSTRUCTIONS, style=styles.HOME_PAGE_INSTRUCTIONS_STYLE),
    html.Div(
        style=styles.HOME_PAGE_DROPDOWN_STYLE,
        children=dcc.Dropdown(
            id=dropdown.ID,
            options=dropdown.OPTIONS,
            searchable=dropdown.SEARCHABLE,
            placeholder=dropdown.PLACE_HOLDER,
            value=dropdown.AUTO_COMPLETE
        )
    )
] + TDH_BY_FLOW


