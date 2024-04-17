import os

from src import Parser
from src.api import HHApi

TEST_VACANCIES_FILEPATH = os.path.abspath('data/test_vacancies.json')
VACANCIES_FILEPATH = os.path.abspath('data/vacancies.json')
hh_api = HHApi(TEST_VACANCIES_FILEPATH)

#vacancies = hh_api.load_vacancies('Java')
#[print(f"{v}\n") for v in vacancies]

parser = Parser(TEST_VACANCIES_FILEPATH)
vcn = parser.parse_json()
[print(f"{el}\n") for el in vcn]