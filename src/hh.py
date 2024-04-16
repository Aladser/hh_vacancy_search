import requests
from src import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """
    url = 'https://api.hh.ru/vacancies'
    headers = {'User-Agent': 'HH-User-Agent'}

    def __init__(self, file_worker):
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
