import pytest
from src.api import HHApi


@pytest.fixture
def api():
    return HHApi()


def test_work(api):
    job_count = 30
    vacancies_list = api.load_vacancies('PHP разработчик', job_count, 10000)
    assert len(vacancies_list) == job_count
    assert api.params == 'page:1, per_page:30, order_by:salary_desc, area:113, text:PHP разработчик, salary:10000'
    print()
    [print(f"{vcn}\n") for vcn in vacancies_list]
