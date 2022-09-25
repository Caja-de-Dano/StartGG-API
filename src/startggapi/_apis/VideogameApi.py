import json

from .QueryStrings import videogame_details_query

class VideogameApi:
    """
    This class wraps the Videogame API 
    https://developer.start.gg/reference/videogame.doc.html
    """

    def __init__(self, base_api):
        """
        Initializes a new VideogameApi which uses the base api
        :param BaseApi base_api: the root API object for making all requests.
        """
        self._base = base_api

    def get_videogame_details(
            self,
            id: int,
    ):
        """
        Get all available details for a videogame using the id
        :returns: dict
        """
        data = {
            "variables": {
                "id": str(id)
            },
            "query": videogame_details_query
        }
        response = self._base.raw_request("https://api.start.gg/gql/alpha", data)
        print(response)
        return json.loads(response.content)