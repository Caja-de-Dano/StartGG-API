import json

from .QueryStrings import event_entrants_query, event_base_query

# type Entrant {
    # id: ID
    # event: Event
    # initialSeedNum: Int
    # isDisqualified: Boolean
    # name: String (The entrant name as it appears in bracket: gamerTag of the participant or team name)
    # # Paginated sets for this entrant
    # # Arguments
    # # page: [Not documented]
    # # perPage: [Not documented]
    # # sortType: How to sort these sets
    # # filters: Supported filter options to filter down set results.
    # paginatedSets(
    #   page: Int,
    #   perPage: Int,
    #   sortType: SetSortType,
    #   filters: SetFilters
    # ): SetConnection
    # participants: [Participant]
    # seeds: [Seed]
    # skill: Int
    # standing: Standing (Standing for this entrant given an event. All entrants queried must be in the same event (for now))
    # stream: Streams @deprecated( reason: "DEPRECATED. Use streams instead, which supports multiple stream types and teams." )
    # streams: [Streams]
    # team: Team (Team linked to this entrant, if one exists)
# }
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

    def find_by_event_id(
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
        eb = event_base_query.replace("QUERY_PARAMS", "$eventId: ID!, $page: Int!, $perPage: Int!")
        eb = eb.replace("SEARCH_BY", "id: $eventId")
        eb = eb.replace("RESPONSE_KEYS", """
            id
            name
            entrants(query: {
                page: $page
                perPage: $perPage
            }) {
                pageInfo {
                    total
                    totalPages
                }
                nodes {
                    id
                    name
                    initialSeedNum
                }
            }
        """)
        data = {
            "variables": {
                "perPage": 50,
                "page": 1,
                "eventId": str(event_id)
            },
            "query": eb
        }
        if per_page:
            data["variables"]["per_page"] = per_page
        if page:
            data["variables"]["page"] = page

        response = self._base.raw_request("https://api.start.gg/gql/alpha", data)
        return json.loads(response.content)

    def find_all_by_event_id(self, event_id, per_page=None):
        default_page_size = 50
        all_entrants = []
        if per_page:
            default_page_size = per_page
        response = self.find_by_event_id(event_id, 1, default_page_size)
        all_entrants += response["data"]["event"]["entrants"]["nodes"]
        total_pages = response["data"]["event"]["entrants"]["pageInfo"]["totalPages"]
        for i in range(total_pages+1):
            if i == 0 or i == 1:
                continue
            response = self.find_by_event_id(event_id, i, default_page_size)
            all_entrants += response["data"]["event"]["entrants"]["nodes"]

        return all_entrants
