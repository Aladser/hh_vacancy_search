import pytest
from src.api import HHApi


@pytest.fixture
def api():
    return HHApi()


def test_work(api):
    job_count = 30
    vacancies_list = api.load_vacancies('PHP разработчик', job_count, 10000)
    assert len(vacancies_list) == job_count
    print(api.params)
    print()
    [print(f"{vcn}\n") for vcn in vacancies_list]
