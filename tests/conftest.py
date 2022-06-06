import pytest
import unittest.mock as mock

@pytest.fixture
def mock_post(monkeypatch) -> mock.MagicMock:
    with monkeypatch.context() as m:
        mock_req = mock.MagicMock()
        m.setattr("requests.post", mock_req)

        yield mock_req