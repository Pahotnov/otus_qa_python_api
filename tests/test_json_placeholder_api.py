import pytest

from data.json_placeholder_api_data import JsonPlaceholderApiData


@pytest.mark.parametrize('post_id', JsonPlaceholderApiData.JSON_PLACEHOLDER_IDS)
def test_get_post_by_id(json_placeholder_api, post_id):
    response = json_placeholder_api.get_post_by_id(post_id)
    assert post_id == response.id


def test_get_list_of_posts(json_placeholder_api):
    response = json_placeholder_api.get_posts_list()
    assert len(response) == 100


def test_get_list_of_albums(json_placeholder_api):
    response = json_placeholder_api.get_albums_list()
    assert len(response) == 100


@pytest.mark.parametrize('album_id', JsonPlaceholderApiData.JSON_PLACEHOLDER_IDS)
def test_get_album_by_id(json_placeholder_api, album_id):
    response = json_placeholder_api.get_album_by_id(album_id)
    assert album_id == response.id


def test_create_new_comment(json_placeholder_api):
    response = json_placeholder_api.post_new_comment(JsonPlaceholderApiData.JSON_PLACEHOLDER_COMMENT_PAYLOAD)
    assert JsonPlaceholderApiData.JSON_PLACEHOLDER_COMMENT_PAYLOAD == response
