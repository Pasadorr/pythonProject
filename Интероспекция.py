from pprint import pprint
def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj)

    # Получаем атрибуты объекта
    attributes = dir(obj)

    # Получаем методы объекта (фильтруем только те, что являются методами)
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    # Получаем модуль, к которому принадлежит объект
    module = getattr(obj_type, "__module__", "__main__")

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type.__name__,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info

# Пример использования
number_info = introspection_info(42)
pprint(number_info)
