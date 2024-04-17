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

    def __init__(self, name: str, url: str, area: str, salary_from: str, requirements: str = ''):
        if name == '' or name is None:
            raise ValueError('не указано название вакансии')

        self.__name = name
        self.__url = url if url else ''
        self.__area = area if area else 'не указано'
        self.__requirements = requirements if requirements else ''
        self.__salary_from = salary_from if salary_from else 'не указана'

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def area(self):
        return self.__area

    @property
    def requirements(self):
        return self.__requirements

    @property
    def salary(self):
        return self.__salary_from

    @property
    def salary_numeric_value(self) -> float:
        salary_value = self.__salary_from.split(' ')[0] if self.__salary_from != 'не указана' else 0
        return salary_value

    @property
    def salary_currency(self) -> str:
        return self.__salary_from.split(' ')[1] if self.__salary_from != 'не указана' else False

    @staticmethod
    def is_better_salary(vacancy_1, vacancy_2):
        if vacancy_1.salary_currency != vacancy_2.salary_currency:
            raise ValueError('зарплаты вакансий в разных валютах')
        else:
            return vacancy_1 if vacancy_1.salary_numeric_value > vacancy_2.salary_numeric_value else vacancy_2

    def __str__(self):
        return (f""
          f"Название: {self.__name}\n"
          f"Ссылка:{self.__url}\n"
          f"Место работы: {self.__area}\n"
          f"Зарплата: {self.__salary_from}\n"
          f"Требования: {self.__requirements}")

