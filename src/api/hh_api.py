import requests
from src.api.basic_api import BasicApi
from src import Parser


class HHApi(BasicApi):
    """
        Класс для работы с API HeadHunter -
        подключается к HeadHunter и возвращает список найденных вакансий
    """

    __url = 'https://api.hh.ru/vacancies'
    __headers = {'User-Agent': 'HH-User-Agent'}
    __page_count: int
    __per_page: int
    __params: dict

    def __init__(self):
        self.__page_count = 1
        """число страниц"""
        self.__per_page = 30
        """число вакансий на странице"""
        self.__params = {
            'page': 0,
            'per_page': self.__per_page,
            'order_by': 'salary_desc',
            'area': 113,
            'text': ''
        }

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
        return Parser.parse_obj_to_vacancy_cls_copy(vacancies_obj)

    @property
    def params(self) -> str:
        return ', '.join([f"{key}:{value}" for key, value in self.__params.items()])
