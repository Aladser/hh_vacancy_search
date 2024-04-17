from abc import ABC, abstractmethod


class BasicVacancyConnector(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass
