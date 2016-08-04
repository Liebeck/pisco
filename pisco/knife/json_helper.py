def get_classes(response):
    return response['classes']


def get_methods(response):
    methods = map(lambda clazz: clazz['methods'], response['classes'])
    return methods


def get_code_blocks(response):
    methods = get_methods(response)
    code_blocks = map(lambda method: method['codeBlock'], methods)
    return code_blocks


def get_class_is_private(response):
    classes = get_classes(response)
    is_private = map(lambda clazz: clazz['isPrivate'], classes)
    return is_private
