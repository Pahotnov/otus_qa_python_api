import pytest

from services.dog_service import DogService
from services.json_placeholder_service import JsonPlaceholderService
from services.open_brewery_db_service import BreweryService


@pytest.fixture
def dog_api():
    dog_api = DogService()
    return dog_api


@pytest.fixture
def brewery_api():
    brewery_api = BreweryService()
    return brewery_api


@pytest.fixture
def json_placeholder_api():
    json_placeholder_api = JsonPlaceholderService()
    return json_placeholder_api


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru/"
    )

    parser.addoption(
        "--status",
        default=200,
        choices=[400, 401, 403, 404, 500, 502, 503]
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status")
