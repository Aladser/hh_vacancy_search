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
            'order_by': 'salary_desc', # по убыванию зарплаты
            'area': 113, # Вся Россия
            'text': ''
        }

    def load_vacancies(self, keyword, job_count=None, salary=None) -> list:
        """
        Загружает вакансии с сайта
        :param keyword: фраза для поиска вакансий
        :param job_count: число вакансий
        :param salary: желаемая зарплата
        :return: список Vacancy
        """

        # установка числа вакансий
        if job_count and job_count != '' and job_count > 0:
            self.__params['per_page'] = job_count
        # установка зарплаты
        if salary and salary != "" and salary > 0:
            self.__params['salary'] = salary

        vacancies_obj_list = []
        self.__params['text'] = keyword
        while self.__params.get('page') != self.__page_count:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            resp_vacancies = response.json()['items']
            vacancies_obj_list.extend(resp_vacancies)
            self.__params['page'] += 1
        return Parser.parse_obj_to_vacancy_cls_copy(vacancies_obj_list)

    @property
    def params(self) -> str:
        return ', '.join([f"{key}:{value}" for key, value in self.__params.items()])
