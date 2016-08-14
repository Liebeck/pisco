def get_classes(response):
    return response['classes']


# returns a list of all methods in a class
def get_methods_in_clazz(clazz):
    methods = map(lambda method: method, clazz['methods'])
    return methods
