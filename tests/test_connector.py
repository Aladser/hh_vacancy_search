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
    name_list = ['пилот', 'пилот', 'пилот', 'инженер', 'швея']
    area_list = ['Зея', 'Зея', 'Тында', 'Москва', 'Тверь']
    salary_from = ['1000 RUR', '2000 RUR', '3000 RUR', '3000 RUR', '3000 RUR']

    if connector.vacancy_count < 5:
        for i in range(5):
            vcn_params = {
                'vcn_id': i + 1,
                'name': name_list[i],
                'url': 'https://blagoveschensk.hh.ru/vacancy/93900476',
                'area': area_list[i],
                'salary_from': salary_from[i]
            }
            vacancy = Vacancy(**vcn_params)
            connector.add_vacancy(vacancy)
        assert connector.vacancy_count == 5

    vcn_list = connector.get_vacancies()
    assert len(vcn_list) == 5
    vcn_list = connector.get_vacancies({'name':'пилот'})
    assert len(vcn_list) == 3
    vcn_list = connector.get_vacancies({'name':'пилот', 'area':'Зея'})
    assert len(vcn_list) == 2
    vcn_list = connector.get_vacancies({'name': 'пилот', 'area': 'Зея', 'salary_from': '1000 RUR'})
    print(vcn_list)