class LogMixin:
    """ Информация о классе"""

    def get_props_str(self) -> str:
        """ Словарь атрибутов как строка """

        param_values = ', '.join([f"{key}:{value}" for key, value in self.__dict__.items()])
        return f"{self.__class__.__name__}({param_values})"

    def get_props_dict(self) -> dict:
        """Словарь атрибутов как форматированный словарь"""

        props_dict = {}
        props_list_str = vars(self)
        for key, value in props_list_str.items():
            # приватный или публичный атрибут
            normalized_key = key[key.find('__')+2:] if key.find('__')>-1 else key
            props_dict[normalized_key] = value
        return props_dict

    def log(self) -> None:
        print(self.get_props_str())
