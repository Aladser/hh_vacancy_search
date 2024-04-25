import pytest
from src import Vacancy


@pytest.fixture
def job_params():
    return {
        'vcn_id': 1,
        'name': 'программист',
        'url': 'https://blagoveschensk.hh.ru/vacancy/93900476',
        'area': 'Благовещенск',
        'salary_from': 1000,
        'salary_to': 2000,
        'salary_currency': 'руб',
        'requirement': 'уметь читать'
    }


def test_init(job_params):
    print()
    # все атрибуты заданы
    vacancy = Vacancy(**job_params)
    vacancy_props = vacancy.get_props_dict()
    for key in job_params:
        assert job_params[key] == vacancy_props[key]
    assert vacancy.salary == f"от {job_params['salary_from']} до {job_params['salary_to']} {job_params['salary_currency']}"
    props_str = ("Vacancy(_Vacancy__vcn_id:1, _Vacancy__name:программист, _Vacancy__salary_currency:руб, "
                 "_Vacancy__salary_from:1000, _Vacancy__salary_to:2000, "
                 "_Vacancy__url:https://blagoveschensk.hh.ru/vacancy/93900476, _Vacancy__area:Благовещенск, "
                 "_Vacancy__requirement:уметь читать)")
    assert vacancy.get_props_str() == props_str

    # не заданы атрибуты
    job_params['url'] = None
    job_params['area'] = None
    job_params['requirement'] = None
    vacancy = Vacancy(**job_params)
    assert vacancy.url == 'не указана'
    assert vacancy.area == 'не указано'
    assert vacancy.requirement == ''
    job_params['url'] = ''
    job_params['area'] = ''
    job_params['requirement'] = ''
    vacancy = Vacancy(**job_params)
    assert vacancy.url == 'не указана'
    assert vacancy.area == 'не указано'
    assert vacancy.requirement == ''

    # не указана валюта
    job_params['salary_currency'] = ''
    vacancy = Vacancy(**job_params)
    assert vacancy.salary == 'не указана'
    job_params['salary_currency'] = None
    assert vacancy.salary == 'не указана'

    # не указана зарплата от
    job_params['salary_currency'] = 'руб'
    job_params['salary_from'] = None
    vacancy = Vacancy(**job_params)
    assert vacancy.salary == 'до 2000 руб'
    job_params['salary_from'] = ""
    vacancy = Vacancy(**job_params)
    assert vacancy.salary == 'до 2000 руб'

    # не указана зарплата до
    job_params['salary_from'] = 1000
    job_params['salary_to'] = None
    vacancy = Vacancy(**job_params)
    assert vacancy.salary == 'от 1000 руб'
    job_params['salary_to'] = ""
    vacancy = Vacancy(**job_params)
    assert vacancy.salary == 'от 1000 руб'

    # неположительная зарплата
    job_params['salary_from'] = -1
    with pytest.raises(ValueError, match='Начальная зарплата должна быть положительным числом'):
        Vacancy(**job_params)
    job_params['salary_from'] = 1
    job_params['salary_to'] = -1
    with pytest.raises(ValueError, match='Конечная зарплата должна быть положительным числом'):
        Vacancy(**job_params)

    # нет id и названия
    job_params['vcn_id'] = None
    with pytest.raises(ValueError, match='не указан id вакансии'):
        Vacancy(**job_params)
    job_params['vcn_id'] = 1
    job_params['name'] = None
    with pytest.raises(ValueError, match='не указано название вакансии'):
        Vacancy(**job_params)

def test_work(job_params):
    print()
    # зарплата программист 1 < программист 2
    job_params['name'] = 'программист 1'
    job_params['salary_from'] = 1000
    vacancy_1 = Vacancy(**job_params)
    job_params['vcn_id'] = 2
    job_params['name'] = 'программист 2'
    job_params['salary_from'] = 2000
    vacancy_2 = Vacancy(**job_params)
    assert Vacancy.is_better_salary(vacancy_1, vacancy_2) == vacancy_2

    # зарплата программист 1 > программист 2
    job_params['salary_from'] = 500
    vacancy_2 = Vacancy(**job_params)
    assert Vacancy.is_better_salary(vacancy_1, vacancy_2) == vacancy_1

    # разные валюты
    job_params['salary_currency'] = 'USD'
    vacancy_2 = Vacancy(**job_params)
    assert not Vacancy.is_better_salary(vacancy_1, vacancy_2)

    # зарплата ПОСЛЕ программист 1 > программист 2
    job_params['salary_currency'] = 'руб'
    job_params['salary_from'] = None
    job_params['vcn_id'] = 1
    job_params['name'] = 'программист 1'
    job_params['salary_to'] = 5000
    vacancy_1 = Vacancy(**job_params)
    job_params['vcn_id'] = 2
    job_params['name'] = 'программист 2'
    job_params['salary_to'] = 3000
    vacancy_2 = Vacancy(**job_params)
    assert Vacancy.is_better_salary(vacancy_1, vacancy_2) == vacancy_1

    # зарплата ПОСЛЕ программист 1 < программист 2
    job_params['salary_to'] = 2000
    vacancy_1 = Vacancy(**job_params)
    assert Vacancy.is_better_salary(vacancy_1, vacancy_2) == vacancy_2

    # нет зарплат для сравнения
    job_params['salary_to'] = None
    vacancy_1 = Vacancy(**job_params)
    assert not Vacancy.is_better_salary(vacancy_1, vacancy_2)
