from src.api import HHApi
from src import user_interaction

hh_api = HHApi()

if __name__ == "__main__":
    search_params = user_interaction()
    vacancies = hh_api.load_vacancies(**search_params)
    [print(el, end="\n\n") for el in vacancies]
