import pytest
from src.api import HHApi


@pytest.fixture
def api():
    return HHApi()


def test_work(api):
    job_count = 10
    vacancies_list = api.load_vacancies('PHP разработчик', job_count)
    assert len(vacancies_list) == job_count
    print()
    [print(f"{vcn}\n") for vcn in vacancies_list]
