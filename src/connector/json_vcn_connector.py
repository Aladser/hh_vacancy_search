import json
import os.path

from src import Parser, Vacancy
from src.connector.basic_vcn_connector import BasicVacancyConnector


class JSONVacancyConnector(BasicVacancyConnector):
    __file_worker: str
    __parser: Parser

    def __init__(self, file_worker):
        if not os.path.isfile(file_worker):
            raise FileNotFoundError

        self.__file_worker = file_worker
        self.__parser = Parser(file_worker)

    def add_vacancy(self, new_vacancy: Vacancy) -> bool:
        # получение списка объектов вакансий из JSON-файла
        vacanices_obj_list = self.__parser.parse_json()
        # новая вакансия как объект списка объектов вакансий JSON файла
        new_vacancy_json_obj = {
            'id': new_vacancy.vcn_id,
            'name': new_vacancy.name,
            'alternate_url': new_vacancy.url,
            'area': {'name': new_vacancy.area},
            'snippet': {'requirement': new_vacancy.requirements},
            'salary': {
                'from': new_vacancy.salary_numeric_value,
                'currency': new_vacancy.salary_currency
            }
        }

        # сохранение новой вакансии в JSON-файл
        vacanices_obj_list.append(new_vacancy_json_obj)
        json_data = json.dumps({'items': vacanices_obj_list})
        with open(self.__file_worker, 'w') as file:
            file.write(json_data)
        return True

    def delete_vacancy(self, deleted_vacancy_id: int) -> bool:
        # получение списка объектов вакансий из JSON-файла
        vcn_obj_list = self.__parser.parse_json()
        # поиск удаляемого элемента по уникальному id. После нахождения элемента останавливается цикл
        found_index = -1
        for i in range(len(vcn_obj_list)):
            if vcn_obj_list[i]['id'] == deleted_vacancy_id:
                found_index = i
                break
        # удаление элемента и переписать JSON-файл
        if found_index > -1:
            vcn_obj_list.pop(found_index)
            json_data = json.dumps({'items': vcn_obj_list})
            with open(self.__file_worker, 'w') as file:
                file.write(json_data)
            return True
        return False

    @property
    def vacancy_count(self) -> int:
        vacancies_obj_list = self.__parser.parse_json()
        return len(vacancies_obj_list)
