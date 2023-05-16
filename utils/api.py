from utils.http_methods import Http_methods

"""Методы тестирования"""

base_url = 'https://reqres.in/api/register' #базовый url

class Api_person():

    @staticmethod
    def create_person():

        json_create_person = {

            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

        post_url = base_url
        print(post_url)
        result_post = Http_methods.post(post_url, json_create_person)
        print(result_post.text)
        return result_post
