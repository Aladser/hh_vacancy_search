import pytest
from src.connector import JSONVacancyConnector
from src import Vacancy, Parser


@pytest.fixture
def working_file_path():
    return '../data/vacancies.json'


@pytest.fixture
def test_file_path():
    return '../data/test_vacancies.json'


def test_work(working_file_path):
    print()
    connector = JSONVacancyConnector(working_file_path)
    parser = Parser(working_file_path)
    name_list = ['пилот1', 'пилот2', 'пилот3']
    area_list = ['Зея1','Зея2','Зея3']
    salary_from = ['1000 RUR', '2000 RUR', '3000 RUR']

    vcn_params = {
        'vcn_id': 1,
        'name': 'программист',
        'url': 'https://blagoveschensk.hh.ru/vacancy/93900476',
        'area': 'Благовещенск',
        'salary_from': '1000 руб'
    }
    vacancy = Vacancy(**vcn_params)
    initial_count = connector.vacancy_count
    connector.add_vacancy(vacancy)
    vcn_obj_list = parser.parse_json()
    print(vcn_obj_list)
    assert connector.vacancy_count == initial_count + 1
    #connector.delete_vacancy(1)
    #assert connector.vacancy_count == initial_count

    fv = connector.get_vacancies({'name': 'Менеджер по туризму'})
    [print(f"{el}\n") for el in fv]
