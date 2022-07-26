import requests

class BaseApi():
    def __init__(self, api_key):
        self._api_key = api_key

    @property
    def api_key(self):
        return self._api_key

    def raw_request(
            self,
            url: str,
            query_data: dict
    ) -> requests.models.Response:
        response = requests.post(
            url,
            json=query_data,
            headers= {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self._api_key
            }
        )
        return response
