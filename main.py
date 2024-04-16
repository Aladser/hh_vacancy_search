from src import HHApi

VACANCIES_FILEPATH = 'data/vacancies.json'

hh_api = HHApi(VACANCIES_FILEPATH)
hh_api.load_vacancies('java')
print(len(hh_api.vacancies))
