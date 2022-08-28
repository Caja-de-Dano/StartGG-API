import json, time, datetime
from .QueryStrings import query_by_distance, query_by_distance_and_time, tournament_query_by_event_id

class TournamentApi:
    """
    This class wraps the Tournament object query
    https://developer.start.gg/reference/tournament.doc.html
    """

    def __init__(self, base_api):
        """
        Initializes a new TournamentApi which uses the base api
        :param BaseApi base_api: the root API object for making all requests.
        """
        self._base = base_api

    def find_events_by_tournament_slug(
            self,
            tourney_slug: str
    ):
        """
        FUNCTION INFO HERE
        """
        data = {
            "variables": {
                "slug": tourney_slug
            },
            "query": tournament_query_by_event_id
        }
        response = self._base.raw_request("https://api.start.gg/gql/alpha", data)
        return json.loads(response.content)["data"]["tournament"]["events"]

    def find_by_coords(
            self,
            coords: str,
            before_date=None,
            after_date=None,
            page=None,
            per_page=None,
            radius=None
    ):
        """
        This function returns a list of tournaments by a given location
        :param string coords:            Lat,Lng string
        :param int before_date:          epoch timestamp
        :param int after_date:           epoch timestamp
        :param int page:                 page number to pull
        :param int per_page:             page limit
        :param string radius:            50mi / 50km
        """
        data = {
            "variables": {
                "perPage": 5,
                "page": 1,
                "coordinates": coords,
                "radius": "50mi"
            }
        }
        if per_page:
            data["variables"]["perPage"] = per_page
        if page:
            data["variables"]["page"] = page
        if radius:
            data["variables"]["radius"] = radius

        lookup_query = query_by_distance
        if before_date and after_date:
            lookup_query = query_by_distance_and_time
            data["variables"]["beforeDate"] = round(time.mktime(before_date.timetuple()) + before_date.microsecond/1e6)
            data["variables"]["afterDate"] = round(time.mktime(after_date.timetuple()) + after_date.microsecond/1e6)
        data["query"] = lookup_query

        response = self._base.raw_request("https://api.start.gg/gql/alpha", data)
        return json.loads(response.content)

    def find_all_by_coords(self, coords, before_date=None, after_date=None, per_page=None, radius=None):
        default_page_size = 50
        all_tournaments = []
        if per_page:
            default_page_size = per_page
        response = self.find_by_coords(coords, before_date=before_date, after_date=after_date, page=1, per_page=default_page_size, radius=radius)
        print(response)
        if "data" in response:
            all_tournaments += response["data"]["tournaments"]["nodes"]
        if "pageInfo" in response["data"]["tournaments"]:
            total_pages = response["data"]["tournaments"]["pageInfo"]["totalPages"]
            for i in range(total_pages+1):
                if i == 0 or i == 1:
                    continue
                response = self.find_by_coords(coords, before_date=before_date, after_date=after_date, page=i, per_page=default_page_size, radius=radius)
                if "data" in response:
                    all_tournaments += response["data"]["tournaments"]["nodes"]
        return all_tournaments
