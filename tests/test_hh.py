import pytest
from src.api import HHApi


@pytest.fixture()
def vacancies_json_path():
    return '../data/vacancies.json'


@pytest.fixture
def api(vacancies_json_path):
    return HHApi(vacancies_json_path)


def test_init(vacancies_json_path):
    hh_api = HHApi(vacancies_json_path)

    assert hh_api.vacancies == []


def test_work(api):
    vacancies_list = api.load_vacancies('PHP разработчик')
    assert len(vacancies_list) == 30
    print()
    [print(f"{vcn}\n") for vcn in api.vacancies]
