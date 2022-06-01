import pytest

from startggapi import StartGGAPI
from startggapi._apis import TournamentApi

@pytest.mark.common
class TestStartGGAPI:
    def test_require_api_key(self):
        with pytest.raises(ValueError):
            StartGGAPI(None)

    def test_tournament_api_access(self):
        api = StartGGAPI("magic-key")
        assert isinstance(api.tournament, TournamentApi)
