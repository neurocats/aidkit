"""Handle authentication."""
import json

from aidkit.config import SECRET


def authorize(url: str, token: str):
    """Authorize to aidkit service."""
    with open(str(SECRET), 'w') as outfile:
        json.dump(dict(token=token, url=url), outfile)


def _get_secret() -> dict:
    """Obtain already stored aidkit token."""
    try:
        with open(str(SECRET)) as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        raise ConnectionRefusedError(
            'You must register your aidkit token with '
            'aidkit.authorize(url="<Your aidkit url>", token="<Your Token>").'
        )

    return data


def get_url() -> str:
    """Get aidkit url."""
    return _get_secret()['url']


def get_token() -> str:
    """Get aidkit token."""
    return _get_secret()['token']
