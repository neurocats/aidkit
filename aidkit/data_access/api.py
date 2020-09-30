"""Send requests to REST api"""

from typing import List, Dict

import requests

from aidkit.data_access.authentication import get_url, get_token
from aidkit.data_access.utils import path_to_bytes


class RESTApi:
    def post_data(self, zip_path):
        """Upload data."""
        resource = 'aidkit-lite/virtual-sensor/data/upload/'
        url = f'{get_url()}:50000/{resource}'
        response = requests.post(
            url=url,
            headers=self.header,
            files=dict(
                data=path_to_bytes(path=zip_path)
            )
        )
        _error_handling(response, url)

        return response

    def list_data(self) -> List[str]:
        """List uploaded data."""
        resource = 'aidkit-lite/virtual-sensor/data/upload/'
        url = f'{get_url()}:50000/{resource}'
        response = requests.get(
            url=url,
            headers=self.header
        )
        _error_handling(response, url)

        return response.json()

    def post_model(self, model_path: str) -> str:
        """Upload model."""
        resource = 'aidkit-lite/virtual-sensor/model/upload/'
        url = f'{get_url()}:50000/{resource}'
        response = requests.post(
            url=url,
            headers=self.header,
            files=dict(
                model=path_to_bytes(path=model_path)
            )
        )
        _error_handling(response, url)

        return response.json()

    def list_models(self):
        """List uploaded models."""
        resource = 'aidkit-lite/virtual-sensor/model/upload/'
        url = f'{get_url()}:50000/{resource}'
        response = requests.get(
            url=url,
            headers=self.header
        )
        _error_handling(response, url)

        return response.json()

    def get_status(self) -> Dict[str, int]:
        """Get status of running pipelines."""
        resource = 'aidkit-lite/virtual-sensor/analysis/execution/'
        url = f'{get_url()}:50000/{resource}'
        response = requests.get(
            url=url,
            headers=self.header
        )
        _error_handling(response, url)

        return response.json()

    def post_pipeline(self, toml_path: str) -> Dict[str, int]:
        """Start pipeline."""
        resource = 'aidkit-lite/virtual-sensor/analysis/execution/'
        url = f'{get_url()}:50000/{resource}'
        response = requests.post(
            url=url,
            headers=self.header,
            files=dict(
                toml=path_to_bytes(path=toml_path)
            )
        )
        _error_handling(response, url)

        return response.json()

    @property
    def header(self) -> dict:
        """Authorized header."""
        return {"Authorization": f"Bearer {get_token()}"}


def _error_handling(response, url):
    if response.status_code == 401:
        raise ConnectionError(
            f"You are not authorized for {url}. Please check your authentication.")
