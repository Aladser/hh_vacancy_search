import os
from src import Parser

REL_VACANCIES_FILEPATH = 'data/request_vacancies.json'
ABS_VACANCIES_FILEPATH = os.path.abspath(REL_VACANCIES_FILEPATH)

parser = Parser(ABS_VACANCIES_FILEPATH)
vacancies = parser.parse()
[print(f"{el}\n") for el in vacancies]