from abc import ABC, abstractmethod


class BasicApi(ABC):
    @property
    @abstractmethod
    def vacancies(self) -> list:
        pass

    @abstractmethod
    def load_vacancies(self, keyword) -> None:
        pass
