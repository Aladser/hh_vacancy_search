import pytest
from src.connector import JSONVacancyConnector
from src import Vacancy


@pytest.fixture
def working_file_path():
    return '../data/vacancies.json'


@pytest.fixture
def vacancy():
    vcn_params = {
        'vcn_id': 100,
        'name': 'программист',
        'url': 'https://blagoveschensk.hh.ru/vacancy/93900476',
        'area': 'Архара',
        'salary_from': '10000',
        'salary_to': '20000',
        'salary_currency': 'руб'
    }
    return Vacancy(**vcn_params)


def test_work(working_file_path, vacancy):
    print()
    connector = JSONVacancyConnector(working_file_path)
    name_list = ['пилот', 'пилот', 'пилот', 'инженер', 'швея']
    area_list = ['Зея', 'Зея', 'Тында', 'Москва', 'Тверь']
    salary_from = [1000, 2000, 3000, 3000, 3000]

    # пеорезаписываю json-файл тестовыми данными
    for i in range(connector.vacancy_count):
        connector.delete_vacancy()
    for i in range(5):
        vcn_params = {
            'vcn_id': i + 1,
            'name': name_list[i],
            'url': 'https://blagoveschensk.hh.ru/vacancy/93900476',
            'area': area_list[i],
            'salary_from': salary_from[i],
            'salary_to': '10000',
            'salary_currency': 'руб'
        }
        connector.add_vacancy(Vacancy(**vcn_params))

    assert len(connector.get_vacancies()) == 5
    assert len(connector.get_vacancies({'name':'пилот'})) == 3
    assert len(connector.get_vacancies({'name':'пилот', 'area':'Зея'})) == 2
    assert len(connector.get_vacancies({'name': 'пилот', 'area': 'Зея', 'salary_from': 1000})) == 1
    assert len(connector.get_vacancies({'name1': 'пилот'})) == 0
    job_count = connector.vacancy_count
    connector.add_vacancy(vacancy)
    assert len(connector.get_vacancies()) == job_count + 1
    connector.delete_vacancy(100)
    assert len(connector.get_vacancies()) == job_count
    connector.delete_vacancy()
    assert len(connector.get_vacancies()) == job_count -1
