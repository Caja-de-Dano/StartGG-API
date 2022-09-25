from ._apis import BaseApi, TournamentApi, EntrantApi, EventApi, VideogameApi

class StartGGAPI:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("api_key must be set.")
        self._base_api = BaseApi(api_key)
        self._tournament = TournamentApi(self._base_api)
        self._entrant = EntrantApi(self._base_api)
        self._event = EventApi(self._base_api)
        self._videogame = VideogameApi(self._base_api)

    @property
    def tournament(self):
        return self._tournament

    @property
    def event(self):
        return self._event

    @property
    def entrant(self):
        return self._entrant

    @property
    def videogame(self):
        return self._videogame
