# Парсер вакансий hh.ru

* **data**
* **src**
  + **api**
      * ``BasicApi`` абстрактный класс api
        + ``api.load_vacancies()`` - возвращает вакансии с ресурса по заданным параметрам
      * ``HHApi``
  + **connector**
      * ``BasicVacancyConnector`` абстрактный класс коннектора
        - ``connector.add_vacancy()`` - добавляет вакансию в JSON-файл
        - ``connector.get_vacancies()`` - получает вакансии из JSON-файла
        - ``connector.delete_vacancy()`` - удаляет вакансию из JSON-файла
      * ``JSONVacancyConnector``
  + ``LogMixin`` - класс логирования
  + ``Parser``
    * ``parser.parse_json()`` - парсит JSON файл в список объектов
    * ``parser.parse_obj_to_vacancy_cls_copy()`` - парсит список объектов в Vacancy список
  + ``Vacancy``
    - ``Vacancy.is_better_salary()`` - сравнение вакансий по зарплате
    - ``vacancy.id``
    - ``vacancy.name``
    - ``vacancy.url``
    - ``vacancy.area`` - место работы
    - ``vacancy.requirement``
    - ``vacancy.salary_currency`` - валюта зарплаты
    - ``vacancy.salary_numeric_value_from`` заплата от
    - ``vacancy.salary_numeric_value_to`` - зарплата до
    - ``vacancy.salary``полное описание зарплаты
    - ``user_interaction`` - функция интерактива с пользователем
* **tests**
* ``main.py`` - точка входа, интерактив с пользователем
