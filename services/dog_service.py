from base_model.base_model import BaseService
from models.dog_model import DogApiResponseModel, DogApiListResponseModel


class DogService(BaseService):
    def __init__(self):
        self.base_url = 'https://dog.ceo/api'

    def get_all_breeds(self):
        response = self.get(f'{self.base_url}/breeds/list/all')
        return DogApiListResponseModel(**response)

    def get_random_image(self):
        response = self.get(f'{self.base_url}/breeds/image/random')
        return DogApiResponseModel(**response)

    def get_multiple_random_images(self, count: int):
        response = self.get(f'{self.base_url}/breeds/image/random/{count}')
        return DogApiListResponseModel(**response)

    def get_all_images_from_breed(self, breed: str):
        response = self.get(f'{self.base_url}/breed/{breed}/images')
        return DogApiListResponseModel(**response)

    def get_all_sub_breed(self, sub_breed: str):
        response = self.get(f'{self.base_url}/breed/{sub_breed}/list')
        return DogApiListResponseModel(**response)
