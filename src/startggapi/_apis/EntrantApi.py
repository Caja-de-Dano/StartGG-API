import json

from .QueryStrings import event_entrants_query

class EntrantApi:
    """
    This class wraps the Entrant query
    """

    def __init__(self, base_api):
        """
        Initializes a new EntrantApi which uses the base api
        :param BaseApi base_api: the root API object for making all requests.
        """
        self._base = base_api

    def find_all(
        self,
        event_id: int,
        page: int=None,
        per_page: int=None,
        ) -> dict:
        """
        This function returns a list of tournaments by a given location
        :param int event_id:             start.gg eventId
        :param int page:                 page number to pull
        :param int per_page:             page limit
        """
        data = {
            "variables": {
                "perPage": 50,
                "page": 1,
                "eventId": str(event_id)
            },
            "query": event_entrants_query
        }
        if per_page:
            data["variables"]["per_page"] = per_page
        if page:
            data["variables"]["page"] = page

        response = self._base.raw_request("https://api.start.gg/gql/alpha", data)
        return json.loads(response.content)
