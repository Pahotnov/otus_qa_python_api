import pytest

from data.brewery_api_data import BreweryApiData


@pytest.mark.parametrize('brewery_id', BreweryApiData.LIST_OF_BREWERY_IDS)
def test_get_brewery(brewery_api, brewery_id):
    response = brewery_api.get_brewery(brewery_id)
    assert brewery_id == response.id


@pytest.mark.parametrize('brewery', BreweryApiData.LIST_OF_BREWERY_IDS)
def test_get_list_of_breweries(brewery_api, brewery):
    response = brewery_api.get_breweries_list()
    assert len(response) > 0
    assert BreweryApiData.LIST_OF_BREWERY_IDS[4] == response[4]['id']


@pytest.mark.parametrize('brewery_id', BreweryApiData.LIST_OF_BREWERY_IDS)
def test_get_list_of_breweries_by_ids(brewery_api, brewery_id):
    response = brewery_api.get_list_of_breweries_by_ids(brewery_id)
    assert brewery_id == response[0]['id']


@pytest.mark.parametrize('brewery_state', BreweryApiData.LIST_OF_BREWERY_STATES)
def test_get_list_of_breweries_by_state(brewery_api, brewery_state):
    response = brewery_api.get_list_of_breweries_by_state(brewery_state)
    assert brewery_state in response[0]['state']


@pytest.mark.parametrize('per_page', [1, 3, 5, 10, 20])
def test_get_list_of_breweries_by_per_page(brewery_api, per_page):
    response = brewery_api.get_list_of_breweries_by_per_page(per_page)
    assert len(response) == per_page
