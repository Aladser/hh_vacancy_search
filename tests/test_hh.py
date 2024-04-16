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
    assert hh_api.params == 'text:, page:0, per_page:10'
    hh_api.set_param('text', 'java')
    with pytest.raises(ValueError):
        hh_api.set_param('key', 'java')
    assert hh_api.get_param('page') == 0


def test_work(api):
    assert len(api.load_vacancies('java')) == 10