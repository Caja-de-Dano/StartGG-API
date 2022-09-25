import pytest
import json
from unittest.mock import MagicMock
from .helpers import FakeResponse

from startggapi._apis import VideogameApi
from startggapi._apis.QueryStrings import event_entrants_query

@pytest.mark.unit
class TestVideogame:
    def test_get_videogame_details(self):
        mock_base_api = MagicMock()
        mock_base_api.raw_request.return_value = FakeResponse()
        test_videogame_id = "1"
        videogame = VideogameApi(mock_base_api)
        expected_return = {}

        ret = videogame.get_videogame_details(test_videogame_id)
        mock_base_api.raw_request.assert_called()
        print(ret)
        assert ret == expected_return


        