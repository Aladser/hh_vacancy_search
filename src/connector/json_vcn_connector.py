import json
import os.path

from src import Parser, Vacancy


class JSONVacancyConnector:
    __file_worker: str
    __parser: Parser

    def __init__(self, file_worker):
        if not os.path.isfile(file_worker):
            raise FileNotFoundError

        self.__file_worker = file_worker
        self.__parser = Parser(file_worker)

    def add_vacancy(self, new_vacancy: Vacancy):
        # получение из JSON-файла списка объектов вакансий
        vacanices_obj_list = self.__parser.parse_json()
        # новая вакансия как объект списка объектов вакансий JSON файла
        new_vacancy_obj = new_vacancy.get_props_dict()
        new_vacancy_json_obj = {
            'name': new_vacancy_obj['name'],
            'alternate_url': new_vacancy_obj['url'],
            'area': {'name': new_vacancy_obj['area']},
            'snippet': {'requirement': new_vacancy_obj['requirements']},
            'salary': {'from': new_vacancy_obj['salary_from']}
        }

        # сохранение новой вакансии в JSON-файл
        vacanices_obj_list.append(new_vacancy_json_obj)
        json_data = json.dumps({'items': vacanices_obj_list})
        with open(self.__file_worker, 'w') as file:
            file.write(json_data)

    def delete_vacancy(self, vacancy: Vacancy):
        pass
