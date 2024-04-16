import json
import os.path


class Parser:
    __file_worker: str

    def __init__(self, file_worker):
        self.__file_worker = file_worker

    def parse(self):
        with open(self.__file_worker) as file:
            resp_data = json.load(file)
        resp_vacancies = resp_data['items']

        for key in resp_vacancies:
            print(key)

if __name__ == '__main__':
    REL_VACANCIES_FILEPATH = '../data/request_vacancies.json'
    ABS_VACANCIES_FILEPATH = os.path.abspath(REL_VACANCIES_FILEPATH)

    parser = Parser(ABS_VACANCIES_FILEPATH)
    parser.parse()