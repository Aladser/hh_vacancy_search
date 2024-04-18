import os

from src.api import HHApi

VACANCIES_FILEPATH = os.path.abspath('data/vacancies.json')
hh_api = HHApi(VACANCIES_FILEPATH)


def user_interaction():
    query_params = {
        'keyword': {
         'query_text': 'Введите поисковый запрос:',
         'type': str,
         'value': None
         },
        'job_count': {
         'query_text': 'Введите количество вакансий для вывода в топ N. Нажмите Enter, чтобы пропустить:',
         'type': int,
         'value': None
         },
        'salary':{
         # глупо указывать диапазон. Кто ставит верхнюю планку зарплате при поиске?)
         'query_text': 'Введите желаемую зарплату. Нажмите Enter, чтобы пропустить:',
         'type': int,
         'value': None
         }
    }

    for key, value in query_params.items():
        if value['type'] == int:
            while True:
                try:
                    user_input = input(value['query_text'])
                    value['value'] = int(user_input)
                except ValueError:
                    print('Не введено число.')
                finally:
                    if isinstance(value['value'], int):
                        break
                    elif user_input == '':
                        value['value'] = None
                        break
                    continue
        else:
            value['value'] = str(input(value['query_text']))

    return {
        'keyword': query_params['keyword']['value'],
        'job_count': query_params['job_count']['value'],
        'salary': query_params['salary']['value']
    }


if __name__ == "__main__":
    search_params = user_interaction()
    vacancies = hh_api.load_vacancies(**search_params)
    [print(f"{el}\n") for el in vacancies]
