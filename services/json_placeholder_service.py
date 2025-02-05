from base_model.base_model import BaseService
from models.json_placeholder_model import JsonPlaceholderApiResponsePostModel, JsonPlaceholderApiResponseAlbumModel, \
    JsonPlaceholderApiRequestCommentModel


class JsonPlaceholderService(BaseService):
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com/'


    def get_post_by_id(self, post_id: int):
        response = self.get(f'{self.base_url}/posts/{post_id}')
        return JsonPlaceholderApiResponsePostModel(**response)

    def get_posts_list(self):
        response = self.get(f'{self.base_url}/posts')
        return response

    def get_albums_list(self):
        response = self.get(f'{self.base_url}/albums')
        return response

    def get_album_by_id(self, album_id: int):
        response = self.get(f'{self.base_url}/albums/{album_id}')
        return JsonPlaceholderApiResponseAlbumModel(**response)

    def post_new_comment(self, payload):
        response = self.post(f'{self.base_url}/comments', data=payload)
        return response
