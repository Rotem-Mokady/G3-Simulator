from dash import (
    Dash,
    html,
)
from configs.site.settings import BROWSER_WINDOW_NAME


app = Dash(BROWSER_WINDOW_NAME)
app.layout = html.Div(style={
    'background-image': 'url("diginex.png")',
})