from src.log_mixin import LogMixin


class Vacancy(LogMixin):
    """
    Вакансия
    :param vcn_id: id
    :param name: название
    :param url: адрес вакансии
    :param area: место работы
    :param requirement: требования
    :param salary_from: зарплата от
    :param salary_to: зарплата до
    :param salary_currency: валюта зарплаты
    """

    __vcn_id: int
    __name: str
    __url: str
    __area: str
    __requirement: str
    __salary_from: int
    __salary_to: int
    __salary_currency: str

    def __init__(
            self, vcn_id: int, name: str, url: str, area: str,
            salary_from: str, salary_to: str, salary_currency: str,
            requirement: str = ''
    ):
        # проверка id и названия
        if name == '' or name is None:
            raise ValueError('не указано название вакансии')
        if vcn_id == '' or vcn_id is None:
            raise ValueError('не указан id вакансии')

        self.__vcn_id = vcn_id
        self.__name = name

        # проверка зарплаты
        if salary_currency and salary_currency != '' and (salary_from or salary_to):
            self.__salary_currency = salary_currency

            # начальная зарплата
            if salary_from and salary_from != '':
                salary_from = int(salary_from)
                if salary_from < 0:
                    raise ValueError('Начальная зарплата должна быть положительным числом')
                self.__salary_from = salary_from
            else:
                self.__salary_from = None

            # конечная зарплата
            if salary_to and salary_to:
                salary_to = int(salary_to)
                if salary_to < 0:
                    raise ValueError('Конечная зарплата должна быть положительным числом')
                self.__salary_to = salary_to
            else:
                self.__salary_to = None
        else:
            self.__salary_currency = None
            self.__salary_from = None
            self.__salary_to = None

        self.__url = url if url else 'не указана'
        self.__area = area if area else 'не указано'
        self.__requirement = requirement if requirement else ''

    @property
    def id(self) -> int:
        return int(self.__vcn_id)

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
    def requirement(self):
        return self.__requirement

    @property
    def salary_currency(self) -> str:
        return self.__salary_currency

    @property
    def salary_numeric_value_from(self) -> int:
        return self.__salary_from

    @property
    def salary_numeric_value_to(self) -> int:
        return self.__salary_to

    @property
    def salary(self) -> str:
        if self.__salary_currency:
            if self.__salary_from and self.__salary_to:
                return f"от {self.__salary_from} до {self.__salary_to} {self.__salary_currency}"
            elif self.__salary_from:
                return f"от {self.__salary_from} {self.__salary_currency}"
            elif self.__salary_to:
                return f"до {self.__salary_to} {self.__salary_currency}"
        else:
            return 'не указана'

    @staticmethod
    def is_better_salary(vacancy_1, vacancy_2):
        if vacancy_1.salary_currency != vacancy_2.salary_currency:
            try:
                raise ValueError
            except ValueError:
                print('Зарплаты вакансий в разных валютах')
            finally:
                return False

        vcn1_salary_from = vacancy_1.salary_numeric_value_from
        vcn2_salary_from = vacancy_2.salary_numeric_value_from
        vcn1_salary_to = vacancy_1.salary_numeric_value_to
        vcn2_salary_to = vacancy_2.salary_numeric_value_to
        if vcn1_salary_from and vcn2_salary_from:
            return vacancy_1 if vcn1_salary_from > vcn2_salary_from else vacancy_2
        elif vcn1_salary_to and vcn2_salary_to:
            return vacancy_1 if vcn1_salary_to > vcn2_salary_to else vacancy_2
        else:
            try:
                raise ValueError
            except ValueError:
                print('Нет данных для корректного сравнения зарплат')
            finally:
                return False

    def __str__(self):
        return (f""
                f"id:{self.__vcn_id}\n"
                f"Название: {self.__name}\n"
                f"Ссылка:{self.__url}\n"
                f"Место работы: {self.__area}\n"
                f"Зарплата: {self.salary}\n"
                f"Требования: {self.__requirement}"
                )
