import json
from src.vacancy import Vacancy


class Parser:
    __file_worker: str

    def __init__(self, file_worker):
        self.__file_worker = file_worker

    def parse_json(self) -> list:
        """парсинг профессий из JSON-файла"""
        with open(self.__file_worker) as file:
            file_line_count = sum([1 for line in file])
        if file_line_count > 0:
            with open(self.__file_worker) as file:
                resp_data = json.load(file)
        else:
            return []

        if 'items' in resp_data:
            resp_data = resp_data['items']

        return self.parse_obj(resp_data)

    @staticmethod
    def parse_obj(vacancies_obj: list) -> list:
        """парсинг профессий из объекта"""
        vacancies = []
        for i in range(len(vacancies_obj)):
            vacancy = vacancies_obj[i]
            url = vacancy['alternate_url'] if vacancy['alternate_url'] else None
            area = vacancy['area']['name'] if vacancy['area']['name'] else None
            requirement = vacancy['snippet']['requirement'] if vacancy['snippet']['requirement'] else None
            if vacancy['salary']:
                salary_from = f"от {vacancy['salary']['from']} {vacancy['salary']['currency']}"
            else:
                salary_from = None
            vacancies.append(Vacancy(vacancy['name'], url, area, salary_from, requirement))

        return vacancies
