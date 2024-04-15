import pytest
from classes.vacancy.vacancy import JobRequirements


@pytest.fixture
def requirement_params():
    return {
        'activity_field': 'IT',
        'employment_type': 'удаленная',
        'education': 'не имеет значения',
        'experience': 'не имеет значения',
    }


def test_init(requirement_params):
    job_requirements = JobRequirements(**requirement_params)
    jr_props_dict = job_requirements.get_props_dict()
    for key in requirement_params:
        assert requirement_params[key] == jr_props_dict[key]
