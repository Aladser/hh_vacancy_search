from classes.log_mixin import LogMixin


class JobRequirements(LogMixin):
    """Требования вакансии
       :param activity_field: сфера деятельности
       :param employment_type: тип занятости
       :param education: образование
       :param experience: опыт работы
    """

    __activity_field: str
    __employment_type: str
    __education: str
    __experience: str

    def __init__(self, activity_field: str, employment_type: str, education: str, experience: str):
        self.__activity_field = activity_field
        self.__employment_type = employment_type
        self.__education = education
        self.__experience = experience


