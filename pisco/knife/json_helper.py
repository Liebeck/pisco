def get_classes(response):
    return response['classes']


# returns a list of all methods in a class
def get_methods_in_clazz(clazz):
    methods = map(lambda method: method, clazz['methods'])
    return methods


# return a list of boolean for each class, bool = class is access_modifier
def get_clazzes_is_access_modifier(response, access_modifier):
    classes = get_classes(response)
    is_access_modifier_by_clazz = map(lambda clazz:
                                      clazz[access_modifier],
                                      classes)
    return is_access_modifier_by_clazz
