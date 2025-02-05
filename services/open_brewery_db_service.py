from base_model.base_model import BaseService
from models.brewery_model import BreweryModelResponse


class BreweryService(BaseService):
    def __init__(self):
        self.base_url = 'https://api.openbrewerydb.org/v1/breweries'

    def get_brewery(self, brewery_id: str):
        response = self.get(f'{self.base_url}/{brewery_id}')
        return BreweryModelResponse(**response)

    def get_breweries_list(self):
        response = self.get(self.base_url)
        return response

    def get_list_of_breweries_by_ids(self, ids: str):
        response = self.get(f'{self.base_url}', params={'by_ids': ids})
        return response

    def get_list_of_breweries_by_state(self, state: str):
        response = self.get(f'{self.base_url}', params={'by_state': state})
        return response

    def get_list_of_breweries_by_per_page(self, per_page: int):
        response = self.get(f'{self.base_url}', params={'per_page': per_page})
        return response
