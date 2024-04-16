import pytest
from src import HHApi


@pytest.fixture()
def vacancies_json_path():
    return '../data/vacancies.json'


def test_work(vacancies_json_path):
    hh_api = HHApi(vacancies_json_path)

    assert hh_api.params == 'text:, page:0, per_page:10'
    hh_api.set_param('text', 'java')
    with pytest.raises(ValueError):
        hh_api.set_param('key', 'java')