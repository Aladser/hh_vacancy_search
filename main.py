from src import HH

VACANCIES_FILEPATH = 'data/vacancies.json'

hh_api = HH(VACANCIES_FILEPATH)
hh_api.load_vacancies('java')
print(len(hh_api.vacancies))
