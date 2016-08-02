def get_classes(response):
    # print response['classes']
    return response['classes']


def get_methods(response):
    methods = map(lambda clazz: clazz['methods'], response['classes'])
    # print methods
    return methods
