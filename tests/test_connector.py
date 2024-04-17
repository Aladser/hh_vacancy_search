import pytest
from src.connector import JSONVacancyConnector
from src import Vacancy, Parser


@pytest.fixture
def filepath():
    return '../data/vacancies.json'


@pytest.fixture
def connector(filepath):
    return JSONVacancyConnector(filepath)


def test_work(connector):
    print()
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
    assert connector.vacancy_count == initial_count + 1
    connector.delete_vacancy(1)
    assert connector.vacancy_count == initial_count
