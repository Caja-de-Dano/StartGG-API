from ._apis import BaseApi, TournamentApi

class StartGGAPI:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("api_key must be set.")
        self._base_api = BaseApi(api_key)
        self._tournament = TournamentApi(self._base_api)

    @property
    def tournament(self):
        return self._tournament
    