import requests
from src.api.basic_api import BasicApi
from src import Parser


class HHApi(BasicApi, Parser):
    """
    Класс для работы с API HeadHunter
    :param page_count: число страниц запроса
    :param per_page: количество элементов страницы
    """

    __url = 'https://api.hh.ru/vacancies'
    __headers = {'User-Agent': 'HH-User-Agent'}

    __possible_params_list = [
        'text', 'page', 'per_page', 'search_field', 'employment', 'schedule', 'area', 'professional_role', 'salary',
        'only_with_salary', 'period', 'date_from', 'order_by'
    ]
    __wrong_key_exception_msg_end = ' - недопустимый ключ'

    __page_count: int
    __per_page: int
    __params: dict
    __vacancies: list

    def __init__(self, file_worker, page_count=1, per_page=10):
        self.__page_count = page_count
        self.__per_page = per_page
        self.__params = {'text': '', 'page': 0, 'per_page': self.__per_page, 'order_by': 'salary_desc'}
        self.__vacancies = []
        super().__init__(file_worker)

    @property
    def vacancies(self) -> list:
        return self.__vacancies

    @property
    def params(self) -> str:
        return ', '.join([f"{key}:{value}" for key, value in self.__params.items()])

    def get_param(self, key):
        if key not in self.__params:
            raise ValueError(f"{key}{self.__wrong_key_exception_msg_end}")

        return self.__params[key]

    def set_param(self, key: str, value: str = None) -> None:
        if key not in self.__possible_params_list:
            raise ValueError(f"{key}{self.__wrong_key_exception_msg_end}")

        self.__params[key] = value

    def load_vacancies(self, keyword) -> list:
        vacancies_obj = []
        self.__params['text'] = keyword
        while self.__params.get('page') != self.__page_count:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            vacancies_obj.extend(vacancies)
            self.__params['page'] += 1
            print()
        self.__vacancies = self.parse_obj_to_vacancy_cls_copy(vacancies_obj)
        return self.__vacancies


"""
    ключи JSON-файла
    page - номер страницы
    per_page- количество элементов
    text - Переданное значение ищется в полях вакансии, указанных в параметре search_field
    search_field - Область поиска. Справочник с возможными значениями: vacancy_search_fields в /dictionaries. 
    По умолчанию, используются все поля. Можно указать несколько значений
    employment -Тип занятости. Необходимо передавать id из справочника employment в /dictionaries.
    schedule - График работы. Необходимо передавать id из справочника schedule в /dictionaries.
    area - Регион. Необходимо передавать id из справочника /areas. Можно указать несколько значений
    professional_role - Профессиональная область. Необходимо передавать id из справочника /professional_roles
    salary - Размер заработной платы. Если указано это поле, но не указано currency, то для currency используется значение RUR. 
При указании значения будут найдены вакансии, в которых вилка зарплаты близка к указанной в запросе. 
При этом значения пересчитываются по текущим курсам ЦБ РФ. Например, при указании salary=100&currency=EUR будут найдены вакансии, 
где вилка зарплаты указана в рублях и после пересчёта в Евро близка к 100 EUR. По умолчанию будут также найдены вакансии, 
в которых вилка зарплаты не указана, чтобы такие вакансии отфильтровать, используйте only_with_salary=true
    only_with_salary - Показывать вакансии только с указанием зарплаты. По умолчанию false
    period - Количество дней, в пределах которых производится поиск по вакансиям
    date_from - Дата, которая ограничивает снизу диапазон дат публикации вакансий. Нельзя передавать вместе с параметром period. 
Значение указывается в формате ISO 8601 - YYYY-MM-DD или с точность до секунды YYYY-MM-DDThh:mm:ss±hhmm. 
Указанное значение будет округлено до ближайших пяти минут
    order_by - Сортировка списка вакансий. Справочник с возможными значениями: vacancy_search_order в /dictionaries. 
Если выбрана сортировка по удалённости от гео-точки distance, необходимо также задать её координаты: sort_point_lat, sort_point_lng
"""
