import requests



"""Список HTTP методов"""

class Http_methods:
    headers = {'Content-type': 'application/json'} #Все наши заголовки будут передоваться в формате json
    cookie = ""  #Информация для того чтобы система её запоминала, нужен для  методов для авторизации

    @staticmethod  #Метод нужен для того чтобы не привязываться к этому классу а вызывать эти методы в любом классе и тесте
    def get(url):
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result