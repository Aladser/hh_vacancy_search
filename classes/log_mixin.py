class LogMixin:
    """ Вывод информации в консоль о том, что был создан объект"""
    def get_props_str(self) -> str:
        """ Класс ([атрибуты])"""
        param_values = ""
        for key, value in self.__dict__.items():
            param_values += f"{key}:{value}, "
        if len(self.__dict__.values()) > 0:
            param_values = param_values[:-2]
        return f"{self.__class__.__name__}({param_values})"

    def get_props_dict(self) -> dict:
        """словарь атрибутов"""
        props_dict = {}
        props_list_str = vars(self)
        for key, value in props_list_str.items():
            norm_key = key[key.index('__')+2:]
            props_dict[norm_key] = value
        return props_dict

    def log(self):
        print(self.get_props_str())
