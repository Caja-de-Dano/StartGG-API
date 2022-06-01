class TournamentApi:
    """
    This class wraps the Tournaments query
    """

    def __init__(self, base_api):
        """
        Initializes a new TournamentApi which uses the base api
        :param BaseApi base_api: the root API object for making all requests.
        """
        self._base = base_api

    def by_location(self, coords: str):
        """
        This function returns a list of tournaments by a given location
        :param string coords:    Lat,Lng string
        """
        return True
