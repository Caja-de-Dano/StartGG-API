import pytest
import json
from unittest.mock import MagicMock
from .helpers import FakeResponse

from startggapi._apis import EntrantApi
from startggapi._apis.QueryStrings import event_entrants_query

@pytest.mark.unit
class TestEntrant:
    def test_fetch_entrant_list(self):
        mock_base_api = MagicMock()
        mock_base_api.raw_request.return_value = FakeResponse()
        test_event_id = "736029"
        entrant = EntrantApi(mock_base_api)
        expected_data = {
            "variables": {
                "perPage": 50,
                "page": 1,
                "eventId": test_event_id
            },
            "query": event_entrants_query
        }
        expected_return = {}

        ret = entrant.find_all(test_event_id)

        mock_base_api.raw_request.assert_called_once_with(
            "https://api.start.gg/gql/alpha",
            expected_data
        )
        assert ret == expected_return