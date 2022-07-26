import pytest
import json
from unittest.mock import MagicMock
from .helpers import FakeResponse

from startggapi._apis import EventApi
from startggapi._apis.QueryStrings import event_details_query

@pytest.mark.unit
class TestEventApi:
    def test_fetch_entrant_details(self):
        mock_base_api = MagicMock()
        mock_base_api.raw_request.return_value = FakeResponse()
        test_event_id = "tournament-event-id"
        event = EventApi(mock_base_api)
        expected_data = {
            "variables": {
                "eventId": test_event_id
            },
            "query": event_details_query
        }
        expected_return = {}

        ret = event.get_event_details(test_event_id)

        mock_base_api.raw_request.assert_called_once_with(
            "https://api.start.gg/gql/alpha",
            expected_data
        )
        assert ret == expected_return

