from src import HH

VACANCIES_FILEPATH = 'data/vacancies.json'

hh_api = HH(VACANCIES_FILEPATH)
print(hh_api.params)
