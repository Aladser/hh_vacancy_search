import json
import re
from src.vacancy import Vacancy


class Parser:
    @staticmethod
    def parse_json(file_worker) -> list:
        """парсинг профессий из JSON-файла"""
        with open(file_worker) as file:
            file_line_count = sum([1 for line in file])
        if file_line_count > 0:
            with open(file_worker) as file:
                resp_data = json.load(file)
        else:
            return []

        if 'items' in resp_data:
            resp_data = resp_data['items']

        return resp_data

    @staticmethod
    def parse_obj_to_vacancy_cls_copy(vacancy_dict_list: list) -> list:
        """парсинг профессий из объекта"""
        vacancies = []
        for i in range(len(vacancy_dict_list)):
            vacancy = vacancy_dict_list[i]
            job_params = {
                'vcn_id': vacancy['id'],
                'name': vacancy['name'],
                'url': vacancy['alternate_url'] if vacancy['alternate_url'] else None,
                'area': vacancy['area']['name'] if vacancy['area'] else None,
                'requirement': re.sub(r'\<[^>]*\>', '', vacancy['snippet']['requirement']) if vacancy['snippet']['requirement'] else None,
            }
            if vacancy['salary']:
                job_params['salary_from'] = vacancy['salary']['from'] if vacancy['salary']['from'] else ''
                job_params['salary_to'] = vacancy['salary']['to'] if vacancy['salary']['to'] else ''
                job_params['salary_currency'] = vacancy['salary']['currency'] if vacancy['salary']['currency'] else ''
            else:
                continue
            vacancies.append(Vacancy(**job_params))

        return vacancies
