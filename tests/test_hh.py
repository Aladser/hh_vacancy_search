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
    hh_api.set_param('text', 'java')
    with pytest.raises(ValueError):
        hh_api.set_param('key', 'java')
    assert hh_api.get_param('page') == 0


def test_work(api):
    vacancies_list = api.load_vacancies('python')
    assert len(vacancies_list) == 10
    print()
    [print(f"{job}\n") for job in vacancies_list]
