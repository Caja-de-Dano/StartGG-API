import pytest, datetime
from startggapi import StartGGAPI

@pytest.mark.common
@pytest.mark.unit
def test_search_by_coords_and_time():
    before_date = datetime.datetime.now() - datetime.timedelta(days=12)
    after_date = datetime.datetime.now() - datetime.timedelta(days=14)
    api = StartGGAPI("FAKE_KEY")
    response = api.tournament.find_by_coords("38.61593,-121.4760205", before_date=before_date, after_date=after_date)
    assert len(response['data']['tournaments']['nodes']) is 2

# def test_find_by_coords_with_defaults():
    # just send with coords

# def test_find_by_coords_with_limit():
    # just send with coords
