import pytest
from classes.vacancy.vacancy import Vacancy


@pytest.fixture
def vcn_params():
    return {
        'name': 'программист',
        'url': 'https://blagoveschensk.hh.ru/vacancy/96583143?query=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82&hhtmFrom=vacancy_search_list',
        'description': 'В веб-студию Z-Labs, в связи с расширением, требуются веб-программисты.',
        'salary': 70000,
        'requirements': None
    }


def test_init(vcn_params):
    vcn = Vacancy(**vcn_params)
    vcn_props_dict = vcn.get_props_dict()
    for key in vcn_params:
        assert vcn_params[key] == vcn_props_dict[key]

