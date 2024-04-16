import pytest
from src import Vacancy


@pytest.fixture
def vcn_params():
    return {
        'name': 'программист',
        'url': 'https://blagoveschensk.hh.ru/vacancy/93900476',
        'area': 'Благовещенск',
        'salary_from': '1000 руб'
    }


def test_init(vcn_params):
    # все атрибуты заданы
    vacancy = Vacancy(**vcn_params)
    vacancy_props = vacancy.get_props_dict()
    for key in vcn_params:
        assert vcn_params[key] == vacancy_props[key]
    assert vacancy.salary == vcn_params['salary_from']
    salary_list = vcn_params['salary_from'].split(' ')
    assert vacancy.salary_numeric_value == salary_list[0]
    assert vacancy.salary_currency == salary_list[1]

    # не заданы атрибуты
    vcn_params['url'] = None
    vcn_params['area'] = None
    vcn_params['requirements'] = None
    vcn_params['salary_from'] = None
    vacancy = Vacancy(**vcn_params)
    vacancy_props = vacancy.get_props_dict()
    assert vacancy_props['url'] == ''
    assert vacancy_props['area'] == 'не указано'
    assert vacancy_props['requirements'] == ''
    assert vacancy_props['salary_from'] == 'не указана'

    # не задано название
    vcn_params['name'] = None
    with pytest.raises(ValueError):
        Vacancy(**vcn_params)


def test_work(vcn_params):
    vacancy_1 = Vacancy(**vcn_params)
    vcn_params['name'] = 'программист 2'
    vcn_params['salary_from'] = '2000 руб'
    vacancy_2 = Vacancy(**vcn_params)
    better_vacancy = Vacancy.is_better_salary(vacancy_1, vacancy_2)
    assert better_vacancy.name == 'программист 2'
