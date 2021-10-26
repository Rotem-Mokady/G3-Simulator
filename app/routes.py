from flask import (
    Flask,
    redirect,
    request,
    url_for,
    render_template,
)
from flask_login import (
    current_user,
    login_user,
)
from oauthlib.oauth2 import WebApplicationClient
from dash import (
    Dash,
    html,
)
from app.utils.google_auth import get_authorization_endpoint, get_google_provider_cfg, parse_token, get_user_info
from app.utils.dash_components import add_modules_components_factory
from app.user_auth import User
from configs.dash import (
    styles,
    titles,
    tags,
    google_auth,
    routes,
)


def add_index(server: Flask) -> None:
    @server.route(routes.BluePrints.INDEX)
    def index():
        if current_user.is_authenticated:
            return redirect(url_for(routes.BluePrints.DASH))
        else:
            return redirect(url_for(routes.BluePrints.LOGIN.replace("/", "")))


def add_login(server: Flask, client: WebApplicationClient) -> None:
    @server.route(routes.BluePrints.LOGIN)
    def login():
        # Use library to construct the request for Google login and provide
        # scopes that let you retrieve user's profile from Google
        request_uri = client.prepare_request_uri(
            get_authorization_endpoint(),
            redirect_uri=request.base_url + routes.BluePrints.CALLBACK,
            scope=google_auth.REQUEST_URI_SCOPE,
        )
        return redirect(request_uri)


def add_callback(server: Flask, client: WebApplicationClient) -> None:
    @server.route(routes.BluePrints.LOGIN + routes.BluePrints.CALLBACK)
    def callback():
        google_provider_cfg = get_google_provider_cfg()
        parse_token(google_provider_cfg, client)
        user_info = get_user_info(google_provider_cfg, client)
        if not user_info.get(google_auth.USER_INFO_EMAIL_VERIFIED_KEY):
            unique_id = user_info[google_auth.USER_INFO_UNIQUE_ID_KEY]
            users_email = user_info[google_auth.USER_INFO_EMAIL_ADDRESS_KEY]
            picture = user_info[google_auth.USER_INFO_PICTURE_KEY]
            users_name = user_info[google_auth.USER_INFO_NAME_KEY]
        else:
            return render_template("403.html")
            # return google_auth.EMAIL_IS_NOT_VERIFIED_RESPONSE

        # Create a user in your db with the information provided
        # by Google
        user = User(
            user_id=unique_id, user_name=users_name, email=users_email, profile_pic=picture
        )

        # Doesn't exist? Add it to the database.
        if not User.get(unique_id):
            User.create(user_id=unique_id, user_name=users_name, email=users_email, profile_pic=picture)

        # Begin user session by logging the user in
        login_user(user)
        # Send user back to homepage
        return redirect(url_for(routes.HOME_ROUTE))


def add_dash(server: Flask) -> None:
    @add_modules_components_factory(server=server)
    def create_dash(app: Flask) -> Dash:
        dash_app: Dash = Dash(server=app, url_base_pathname=routes.BluePrints.DASH)
        dash_app.title = titles.TAB_WINDOW_NAME
        dash_app.layout = html.Div(style=styles.BACKGROUND_STYLE, children=tags.FINAL_LAYOUT)
        return dash_app
    create_dash()

