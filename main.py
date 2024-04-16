import os

from src import Parser
from src.api import HHApi

VACANCIES_FILEPATH = os.path.abspath('data/request_vacancies.json')
hh_api = HHApi(VACANCIES_FILEPATH)

vacancies = hh_api.load_vacancies('Java')
print(len(vacancies))