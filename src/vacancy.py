from src.log_mixin import LogMixin


class Vacancy(LogMixin):
    """
    Вакансия
    :param name: название
    :param url: ссылка на вакансию
    :param description: описание
    :param salary: зарплата
    :param requirements: требования
    """

    __name: str
    __url: str
    __description: str
    __salary: int
    __requirements: str

    def __init__(self, name: str, url: str, description: str, salary: int, requirements: str):
        self.__name = name
        self.__url = url
        self.__description = description
        self.__salary = salary
        self.__requirements = requirements
