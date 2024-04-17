import pytest
from src.connector import JSONVacancyConnector
from src import Vacancy, Parser


@pytest.fixture
def filepath():
    return '../data/vacancies.json'


@pytest.fixture
def connector(filepath):
    return JSONVacancyConnector(filepath)


def test_work(connector, filepath):
    print()
    vcn_params = {
        'vcn_id': 1,
        'name': 'программист',
        'url': 'https://blagoveschensk.hh.ru/vacancy/93900476',
        'area': 'Благовещенск',
        'salary_from': '1000 руб'
    }
    vacancy = Vacancy(**vcn_params)
    parser = Parser(filepath)
    connector.add_vacancy(vacancy)
    [print(el) for el in parser.parse_json()]