from src.log_mixin import LogMixin


class Vacancy(LogMixin):
    """
    Вакансия
    :param name: название
    :param url: ссылка на вакансию
    :param area: место работы
    :param salary_from: зарплата от
    :param requirements: требования
    """

    __name: str
    __url: str
    __area: str
    __salary_from: str
    __requirements: str

    def __init__(self, name: str, url: str, area: str, salary_from: str, requirements: str):
        self.__name = name
        self.__url = url
        self.__area = area
        self.__salary_from = salary_from
        self.__requirements = requirements

    def __str__(self):
        return (f""
          f"Название: {self.__name}\n"
          f"Ссылка:{self.__url}\n"
          f"Место работы: {self.__area}\n"
          f"Зарплата: {self.__salary_from}\n"
          f"Требования: {self.__requirements}")
