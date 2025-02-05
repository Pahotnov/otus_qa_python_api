import pytest

from data.brewery_api_data import BreweryApiData


@pytest.mark.parametrize('brewery_id', BreweryApiData.LIST_OF_BREWERY_IDS)
def test_get_brewery(brewery_api, brewery_id):
    response = brewery_api.get_brewery(brewery_id)
    assert brewery_id == response.id


def test_get_list_of_breweries(brewery_api):
    response = brewery_api.get_breweries_list()
    assert BreweryApiData.LIST_OF_BREWERY_IDS[4] == response[4]['id']


@pytest.mark.parametrize('brewery_id', BreweryApiData.LIST_OF_BREWERY_IDS)
def test_get_list_of_breweries_by_ids(brewery_api, brewery_id):
    response = brewery_api.get_list_of_breweries_by_ids(brewery_id)
    assert brewery_id == response[0]['id']


def test_get_list_of_breweries_by_state(brewery_api):
    state = 'California'
    response = brewery_api.get_list_of_breweries_by_state(state)
    assert len(response) == 50


def test_get_list_of_breweries_by_per_page(brewery_api):
    per_page = 5
    response = brewery_api.get_list_of_breweries_by_per_page(per_page)
    assert len(response) == 5
