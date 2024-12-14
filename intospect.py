def introspection_info(obj):
    obj_type = obj.__class__.__name__

    attributes = [attr for attr in dir(obj) if not attr.startswith('__')]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    module = obj.__class__.__module__

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info


number_info = introspection_info(42)
print(number_info)

list_info = introspection_info([1, 2, 3])
print(list_info)


class CustomClass:
    def __init__(self):
        self.attribute = "value"

    def method(self):
        pass


custom_info = introspection_info(CustomClass())
print(custom_info)
