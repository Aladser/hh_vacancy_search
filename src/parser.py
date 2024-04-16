import json
from src.vacancy import Vacancy


class Parser:
    __file_worker: str

    def __init__(self, file_worker):
        self.__file_worker = file_worker

    def parse(self):
        with open(self.__file_worker) as file:
            resp_data = json.load(file)

        resp_vacancies = []
        for i in range(len(resp_data)):
            vacancy = resp_data['items'][i]
            url = vacancy['alternate_url'] if vacancy['alternate_url'] else None
            area = vacancy['area']['name'] if vacancy['area']['name'] else None
            salary_from = f"от {vacancy['salary']['from']} {vacancy['salary']['currency']}" if vacancy['salary'] else None
            requirement = vacancy['snippet']['requirement'] if vacancy['snippet']['requirement'] else None
            resp_vacancies.append(Vacancy(vacancy['name'], url, area, salary_from, requirement))
        return resp_vacancies
