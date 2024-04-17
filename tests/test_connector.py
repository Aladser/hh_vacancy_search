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
        'name': 'программист',
        'url': 'https://blagoveschensk.hh.ru/vacancy/93900476',
        'area': 'Благовещенск',
        'salary_from': '1000 RUR'
    }
    vacancy = Vacancy(**vcn_params)
    parser = Parser(filepath)
    print(parser.parse_json())
    #connector.add_vacancy(vacancy)
