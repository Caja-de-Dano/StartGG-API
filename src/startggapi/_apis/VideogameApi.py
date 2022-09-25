import json

from .QueryStrings import videogame_details_by_id_query, videogame_details_by_slug_query

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

    def get_videogame_by_id(
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
            "query": videogame_details_by_id_query
        }
        response = self._base.raw_request("https://api.start.gg/gql/alpha", data)
        return json.loads(response.content)

    def get_videogame_by_slug(
            self,
            slug: str,
    ):
        """
        Get all available details for a videogame using the slug
        :returns: dict
        """
        data = {
            "variables": {
                "slug": slug
            },
            "query": videogame_details_by_slug_query
        }
        response = self._base.raw_request("https://api.start.gg/gql/alpha", data)
        print(response)
        return json.loads(response.content)