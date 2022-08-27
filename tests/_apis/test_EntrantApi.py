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
        expected_return = {}

        ret = entrant.find_by_event_id(test_event_id)

        mock_base_api.raw_request.assert_called()
        assert ret == expected_return