import requests
import json
from flask import request
from oauthlib.oauth2 import WebApplicationClient
from typing import (
    Dict,
    Union,
)

from configs.dash import google_auth
from configs import secrets


def get_google_provider_cfg() -> Dict:
    """
    get google provider data.
    """
    response = requests.get(secrets.GOOGLE_DISCOVERY_URL)
    assert response.ok, f"status code: {response.status_code}, reason: {response.reason}"
    return requests.get(secrets.GOOGLE_DISCOVERY_URL).json()


def get_authorization_endpoint() -> str:
    """
    find out what URL to hit for Google login.
    """
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg[google_auth.PROVIDER_ENDPOINT_KEY]
    return authorization_endpoint


def parse_token(provider_cfg: Dict, client: WebApplicationClient) -> None:
    """
    :param provider_cfg: google provider data.
    :param client: auth client that should parse data.
    """
    # generated code from flask user request
    code = request.args.get(google_auth.CODE_KEY_FOR_TOKEN)
    # get authorization code Google sent back to you
    token_endpoint = provider_cfg[google_auth.ENDPOINT_KEY_FOR_TOKEN]
    # prepare and send a request to get tokens
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    # the request itself
    response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(secrets.GOOGLE_CLIENT_ID, secrets.GOOGLE_CLIENT_SECRET),
    )

    assert response.ok, f"status_code: {response.status_code}, reason: {response.reason}"
    # parse the token
    client.parse_request_body_response(json.dumps(response.json()))


def get_user_info(provider_cfg: Dict, client: WebApplicationClient) -> Dict:
    # now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = provider_cfg[google_auth.USER_INFO_KEY]
    uri, headers, body = client.add_token(userinfo_endpoint)
    response = requests.get(uri, headers=headers, data=body)
    assert response.ok, f"status_code: {response.status_code}, reason: {response.reason}"
    return response.json()
