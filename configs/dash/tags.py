from dash import (
    html,
    dcc,
)
from configs.dash import (
    titles,
    styles,
    main_dropdown,
    modules_constants,
)
from configs.calcs.defaults.physical_deafult_params import Pipe


TDH_BY_FLOW = [
    html.Div(
        id=modules_constants.TDHbyFlow.ID,
        children=[
            html.Br(),
            dcc.Input(
                id=modules_constants.TDHbyFlow.Pipe.ID,
                autoComplete=modules_constants.TDHbyFlow.Pipe.AUTO_COMPLETE,
                inputMode=modules_constants.TDHbyFlow.Pipe.MODE,
                min=modules_constants.TDHbyFlow.Pipe.MIN,
                value=modules_constants.TDHbyFlow.Pipe.AUTO_COMPLETE,
                placeholder=modules_constants.TDHbyFlow.Pipe.NAME,
                type=modules_constants.TDHbyFlow.Pipe.TYPE,
                style=styles.BUTTONS_STYLE
            ),
            html.Br(),
            dcc.Input(
                id=modules_constants.TDHbyFlow.Diameter.ID,
                autoComplete=modules_constants.TDHbyFlow.Diameter.AUTO_COMPLETE,
                inputMode=modules_constants.TDHbyFlow.Diameter.MODE,
                min=modules_constants.TDHbyFlow.Diameter.MIN,
                value=modules_constants.TDHbyFlow.Diameter.AUTO_COMPLETE,
                placeholder=modules_constants.TDHbyFlow.Diameter.NAME,
                type=modules_constants.TDHbyFlow.Diameter.TYPE,
                style=styles.BUTTONS_STYLE
            ),
            html.Br(),
            dcc.Dropdown(
                id=modules_constants.TDHbyFlow.PipeType.ID,
                options=[{"label": pipe_type, "value": pipe_type} for pipe_type in Pipe.TYPES_TO_E.keys()],
                searchable=modules_constants.TDHbyFlow.PipeType.SEARCHABLE,
                placeholder=modules_constants.TDHbyFlow.PipeType.NAME,
                value=modules_constants.TDHbyFlow.PipeType.AUTO_COMPLETE,
                style=styles.TDH_BY_FLOW_DROPDOWN_STYLE
            ),
            html.Br(),
            html.Button(
                modules_constants.TDHbyFlow.ActivateButton.NAME,
                id=modules_constants.TDHbyFlow.ActivateButton.ID,
                style=styles.ACTIVATION_BUTTONS_STYLE
            ),
            html.Br(),
            dcc.Graph(
                id=modules_constants.TDHbyFlow.Graph.ID
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
            id=main_dropdown.ID,
            options=main_dropdown.OPTIONS,
            searchable=main_dropdown.SEARCHABLE,
            placeholder=main_dropdown.PLACE_HOLDER,
            value=main_dropdown.AUTO_COMPLETE
        )
    )
] + TDH_BY_FLOW


