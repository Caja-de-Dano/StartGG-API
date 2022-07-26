import pytest

from startggapi._apis import BaseApi

@pytest.mark.common
@pytest.mark.unit
class TestBaseApi:
    def test_raw_request(self, mock_post):
        expected_api_key = "test-api"
        expected_url = "url"
        expected_query_params = {}
        expected_resp = object()

        api = BaseApi(expected_api_key)
        mock_post.return_value = expected_resp
        resp = api.raw_request(expected_url, expected_query_params)

        assert resp is expected_resp

        mock_post.assert_called_once_with(
            expected_url,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer test-api"
            },
            json=expected_query_params
        )
