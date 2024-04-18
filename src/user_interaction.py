def user_interaction():
    """интерактив с пользователем"""
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
            # цифровой параметр
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
            # любой другой тип преобразуется к строке
            value['value'] = str(input(value['query_text']))

    return {
        'keyword': query_params['keyword']['value'],
        'job_count': query_params['job_count']['value'],
        'salary': query_params['salary']['value']
    }

