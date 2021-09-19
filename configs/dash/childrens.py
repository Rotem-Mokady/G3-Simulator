from dash import (
    html,
    dcc,
)
from configs.dash import (
    titles,
    styles,
    dropdown,
)


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
            placeholder=dropdown.PLACE_HOLDER
        )
    )
]
