from utils.http_client import HttpClient


class PoetryDB(HttpClient):

    def __init__(self):
        super().__init__(base_uri="https://poetrydb.org/")
        self.headers = {"Content-Type": "application/json"}

    def get_query(self, query):
        request = self.get()
        request.uri(query)
        request.headers(**self.headers)
        response = request.send()
        return response