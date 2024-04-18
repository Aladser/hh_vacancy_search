import json
import os.path

from src import Parser, Vacancy
from src.connector.basic_vcn_connector import BasicVacancyConnector


class JSONVacancyConnector(BasicVacancyConnector):
    __file_worker: str
    __parser: Parser
    __vacancy_count: int
    __vacancies_obj_list: list

    def __init__(self, file_worker):
        if not os.path.isfile(file_worker):
            raise FileNotFoundError

        self.__file_worker = file_worker
        self.__parser = Parser(file_worker)
        self.__vacancies_obj_list = self.__parser.parse_json()
        self.__vacancy_count = len(self.__vacancies_obj_list)

    @property
    def vacancy_count(self) -> int:
        return self.__vacancy_count

    def add_vacancy(self, new_vacancy: Vacancy) -> bool:
        # новая вакансия как объект списка объектов вакансий JSON файла
        new_vacancy_json_obj = {
            'id': new_vacancy.id,
            'name': new_vacancy.name,
            'alternate_url': new_vacancy.url,
            'area': {'name': new_vacancy.area},
            'snippet': {'requirement': new_vacancy.requirement},
            'salary': {
                'from': new_vacancy.salary_numeric_value_from,
                'to': new_vacancy.salary_numeric_value_to,
                'currency': new_vacancy.salary_currency
            }
        }

        # сохранение новой вакансии в JSON-файл
        self.__vacancies_obj_list.append(new_vacancy_json_obj)
        json_data = json.dumps({'items': self.__vacancies_obj_list})
        with open(self.__file_worker, 'w') as file:
            file.write(json_data)
        self.__vacancy_count += 1
        return True

    def delete_vacancy(self, deleted_vacancy_id: int = None) -> bool:
        if not deleted_vacancy_id:
            # если не указан удаляемый элемент, удаляется последний
            found_index = self.__vacancy_count - 1
        else:
            # поиск удаляемого элемента по уникальному id (первое совпадение)
            found_index = -1
            for i in range(self.__vacancy_count):
                if self.__vacancies_obj_list[i]['id'] == deleted_vacancy_id:
                    found_index = i
                    break

        # удаление элемента и перезапись JSON-файла
        if found_index > -1:
            self.__vacancies_obj_list.pop(found_index)
            json_data = json.dumps({'items': self.__vacancies_obj_list})
            with open(self.__file_worker, 'w') as file:
                file.write(json_data)
            self.__vacancy_count -= 1
            return True
        return False

    def get_vacancies(self, params: dict = None) -> list:
        vacancy_copy_list = self.__parser.parse_obj_to_vacancy_cls_copy(self.__vacancies_obj_list)
        # получение списка объектов вакансий, полученных из списка вакансий класса Vacancy
        vacancies_obj_list = [el.get_props_dict() for el in vacancy_copy_list]

        # поиск вакансий в списке объектов вакансий
        found_vacancies_obj_list = []
        if params:
            for vcn in vacancies_obj_list:
                # флаг совпадения
                is_matching = True
                for par_key, par_value in params.items():
                    if par_key not in vcn:
                        # если такого параметра нет у объекта
                        return []

                    if vcn[par_key] != par_value:
                        # перебор свойств объекта
                        is_matching = False
                        break
                if is_matching:
                    found_vacancies_obj_list.append(vcn)
        else:
            for vcn in vacancies_obj_list:
                found_vacancies_obj_list.append(vcn)

        return found_vacancies_obj_list
