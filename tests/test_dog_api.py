import pytest

from data.dog_api_data import DogApiData


def test_get_list_all_breeds(dog_api):
    response = dog_api.get_all_breeds()
    assert response.status == 'success'


def test_get_random_image(dog_api):
    response = dog_api.get_random_image()
    assert '.jpg' in response.message


@pytest.mark.parametrize('count', [1, 3, 5, 7, 10])
def test_get_display_multiple_random_images(dog_api, count):
    response = dog_api.get_multiple_random_images(count)
    assert len(response.message) == count


@pytest.mark.parametrize('breed', DogApiData.LIST_OF_BREEDS)
def test_get_all_images_from_breed(dog_api, breed):
    response = dog_api.get_all_images_from_breed(breed)
    for b in range(len(response.message)):
        assert breed in response.message[b]


def test_get_all_sub_breed(dog_api):
    response = dog_api.get_all_sub_breed('hound')
    assert DogApiData.LIST_OF_SUBBREEDS == response.message
