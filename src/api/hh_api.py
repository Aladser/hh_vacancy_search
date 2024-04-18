import requests
from src.api.basic_api import BasicApi
from src import Parser


class HHApi(BasicApi, Parser):
    """
        Класс для работы с API HeadHunter
    `   :param file_worker: рабочий JSON-файл
        :param page_count: число страниц
        :param per_page: число вакансий на странице`
    """

    __url = 'https://api.hh.ru/vacancies'
    __headers = {'User-Agent': 'HH-User-Agent'}

    __page_count: int
    __per_page: int
    __params: dict
    __vacancies: list

    def __init__(self, file_worker):
        self.__page_count = 1
        self.__per_page = 30
        self.__params = {
            'page': 0,
            'per_page': self.__per_page,
            'order_by': 'salary_desc',
            'area': 113,
            'text': ''
        }
        self.__vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword, job_count=None, salary=None) -> list:
        # установка числа вакансий
        if job_count and job_count != '' and job_count > 0:
            self.__params['per_page'] = job_count
        if salary and salary != "" and salary > 0:
            self.__params['salary'] = salary

        vacancies_obj = []
        self.__params['text'] = keyword
        while self.__params.get('page') != self.__page_count:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            vacancies_obj.extend(vacancies)
            self.__params['page'] += 1
        self.__vacancies = self.parse_obj_to_vacancy_cls_copy(vacancies_obj)
        return self.__vacancies

    @property
    def vacancies(self) -> list:
        return self.__vacancies

    @property
    def params(self) -> str:
        return ', '.join([f"{key}:{value}" for key, value in self.__params.items()])
