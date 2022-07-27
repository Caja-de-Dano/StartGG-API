import pytest
import json

from unittest.mock import MagicMock

from startggapi._apis import TournamentApi
from startggapi._apis.QueryStrings import query_by_distance

class FakeResponse:
    def __init__(self):
        self.content = "{}"

@pytest.mark.skip()
@pytest.mark.unit
class TestTournamentApi:
    def test_find_by_coords(self):
        test_coords = "1,2"
        mock_base_api = MagicMock()
        mock_base_api.raw_request.return_value = FakeResponse()
        tournament = TournamentApi(mock_base_api)
        expected_data = {
            "variables": {
                "perPage": 5,
                "coordinates": test_coords,
                "radius": "50mi"
            },
            "query": query_by_distance
        }
        expected_return = {}

        ret = tournament.find_by_coords(test_coords)

        mock_base_api.raw_request.assert_called_once_with(
            "https://api.start.gg/gql/alpha",
            expected_data
        )
        assert ret == expected_return

    # def test_find_all_event_ids_by_slug(self):
    #     ret = tournament.find_events_by_tournament_slug("mixed-up-2")
    #     assert ret == 1
