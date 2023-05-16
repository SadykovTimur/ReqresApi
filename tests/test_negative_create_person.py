from requests import Response
from utils.api import Api_person
import json
from utils.checking import Checking


class Test_api_person():


    def test_create_person_negative(self):
        print('метод POST')
        result_post: Response = Api_person.create_person()
        Checking.check_status_code(result_post, 201) #проверка статус кода
        token = json.loads(result_post.text)
        print(list(token))  # это команда нужна для того чтобы найти тело ответа запроса
        Checking.check_json_token(result_post, ['id', 'token'])