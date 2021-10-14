from dash import (
    Dash,
    html,
)
import warnings

from configs.dash import (
    styles,
    titles,
    tags,
    components,
)
from configs.secrets import (
    auth_constants,
    db_constants,
)
from app.utils import add_modules_components


@add_modules_components
def create_app() -> Dash:
    f"""
    Project's tests will run based on the configuration.
    :return: An app object with the basic design and the modules components from the modules folder 
    ({components.COMPONENTS_CURRENT_DIR}).
    """
    warnings.filterwarnings("ignore")

    app = Dash(__name__)
    app.title = titles.TAB_WINDOW_NAME
    app.layout = html.Div(style=styles.BACKGROUND_STYLE, children=tags.FINAL_LAYOUT)

    app.config.suppress_callback_exceptions = True
    app.server.config.update(**auth_constants.SERVER_CONFIG)

    db_constants.SQLiteDB.DB.init_app(app.server)
    auth_constants.LOGIN_MANAGER.init_app(app.server)

    return app
