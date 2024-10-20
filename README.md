# Парсер вакансий hh.ru

Программа, получает информацию о вакансиях с платформы hh.ru в России, сохранят ее в файл и позволяет удобно работать с ней: добавлять, фильтровать, удалять.

### Выходные данные
+ Информация о вакансиях, полученная с разных платформ, сохраненная в JSON-файл.
+ Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.

#### Структура
* **data**
* **src**
  + **api**
      * ``BasicApi`` абстрактный класс api. Требует реализацию загрузки вакансий из ресурса.
        + ``api.load_vacancies()``
      * ``HHApi``- класс получения вакансий из сайта api.hh.ru
  + **connector**
      * ``BasicVacancyConnector`` абстрактный класс коннектора.
        - ``connector.add_vacancy()`` - добавляет вакансию в JSON-файл
        - ``connector.get_vacancies()`` - получает вакансии из JSON-файла
        - ``connector.delete_vacancy()`` - удаляет вакансию из JSON-файла
        - ``connector.vacancy_count()`` - число вакансий
      * ``JSONVacancyConnector``
  + ``LogMixin`` - класс логирования.
      - ``get_props_str()`` - словарь атрибутов как строка
      - ``get_props_dict()`` - словарь атрибутов как форматированный словарь
      - ``log()`` - выводит в консоль атрибуты класса
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
  + ``user_interaction`` - функция интерактива с пользователем
* **tests**
* ``main.py`` - точка входа, интерактив с пользователем
