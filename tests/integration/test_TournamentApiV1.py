import pytest, datetime, os
from startggapi import StartGGAPI

api = StartGGAPI(os.environ.get('START_GG_KEY'))

@pytest.mark.skip()
def test_search_by_coords_and_time():
    before_date = datetime.datetime.now() - datetime.timedelta(days=12)
    after_date = datetime.datetime.now() - datetime.timedelta(days=14)
    response = api.tournament.find_by_coords("38.61593,-121.4760205", before_date=before_date, after_date=after_date)
    assert len(response["data"]["tournaments"]["nodes"]) is 3

@pytest.mark.skip()
def test_attendee_list():
    expected_event_id = 78790
    response = api.entrant.find_all(78790)
    assert response["data"]["event"]["id"] == expected_event_id

@pytest.mark.skip()
def test_event_details():
    expected_event_id = 736029
    response = api.event.find_all_entrants(736029)
    assert len(response) == expected_event_id

# TournamentApi tests
@pytest.mark.skip()
def test_find_by_tourney_slug():
    expected_event_id = 78790
    response = api.tournament.find_events_by_tournament_slug("shine-2018")
    assert type(response) == list
    assert response[0].keys() == ["name", "id"]

def test_find_all_event_ids_by_slug():
    ret = api.tournament.find_events_by_tournament_slug("mixed-up-2")
    event_id = ret[0]["id"]
    print(event_id)
    ret = api.event.fetch_sets(event_id)
    assert type(ret) == list
