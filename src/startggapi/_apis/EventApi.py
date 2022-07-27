import json

from .QueryStrings import event_entrants_query, event_details_query, sets_query_by_event_id

class EventApi:
    """
    This class wraps the Event query
    """

    def __init__(self, base_api):
        """
        Initializes a new EventApi which uses the base api
        :param BaseApi base_api: the root API object for making all requests.
        """
        self._base = base_api

    def get_event_details(
            self,
            event_id: int,
    ):
        """
        Get all available details for an event

        :returns: dict
        """
        data = {
            "variables": {
                "eventId": str(event_id)
            },
            "query": event_details_query
        }
        response = self._base.raw_request("https://api.start.gg/gql/alpha", data)
        return json.loads(response.content)


    def find_all_entrants(
        self,
        event_id: int,
        page: int=None,
        per_page: int=None,
        ):
        """
        This function returns a list of entrants for a given event
        :param int event_id:             start.gg eventId
        :param int page:                 page number to pull
        :param int per_page:             page limit
        """
        entrant_list = []
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
        response_json = json.loads(response.content)
        entrant_list += response_json["data"]["event"]["entrants"]["nodes"]

        current_page = 1
        if response_json['data']['event']['entrants']['pageInfo']['totalPages'] > 1:
            while current_page != response_json['data']['event']['entrants']['pageInfo']['totalPages']:
                current_page += 1
                data["variables"]["page"] = current_page
                response = self._base.raw_request("https://api.start.gg/gql/alpha", data)
                entrant_list += json.loads(response.content)["data"]["event"]["entrants"]["nodes"]

        # TODO: properly handle errors from request / expose bad request details, etc
        #return json.loads(response.content)["data"]["event"]["entrants"]["nodes"]
        return entrant_list

    def fetch_sets(
        self,
        event_id,
        ):
        """
        Returns a list of Sets for the event_id
        :param event_id
        """
        set_list = []
        data = {
            "variables": {
                "eventId": str(event_id)
            },
            "query": sets_query_by_event_id
        }
        response = self._base.raw_request("https://api.start.gg/gql/alpha", data)
        response_json = json.loads(response.content)
        return response_json["data"]["event"]["sets"]["nodes"]
