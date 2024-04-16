from abc import ABC, abstractmethod


class BasicApi(ABC):
    @property
    @abstractmethod
    def vacancies(self) -> list:
        pass

    @abstractmethod
    def load_vacancies(self, keyword) -> None:
        pass

    @abstractmethod
    def get_param(self, key):
        pass

    @abstractmethod
    def set_param(self, key: str, value: str = None) -> None:
        pass

