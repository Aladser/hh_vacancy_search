import pytest
from src.api import HHApi


@pytest.fixture
def api():
    return HHApi()


def test_work(api):
    vacancies_list = api.load_vacancies('PHP разработчик')
    assert len(vacancies_list) == 30
    print()
    [print(f"{vcn}\n") for vcn in vacancies_list]
