from abc import ABC, abstractmethod


class BasicVacancyConnector(ABC):
    @abstractmethod
    def get_vacancies(self, params: dict = None) -> list:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @property
    @abstractmethod
    def vacancy_count(self) -> int:
        pass
