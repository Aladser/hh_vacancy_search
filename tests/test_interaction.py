from src import user_interaction


def test_interaction(monkeypatch):
    params = {'job_count': 10, 'keyword': '10', 'salary': 10}
    monkeypatch.setattr('builtins.input', lambda _: "10")
    assert user_interaction() == params

    params = {'job_count': None, 'keyword': '', 'salary': None}
    monkeypatch.setattr('builtins.input', lambda _: '')
    assert user_interaction() == params
