import json


def get_classes(response):
    return response['classes']


# returns a list of all methods in a file
def get_methods(response):
    methods = map(lambda clazz: clazz['methods'], response['classes'])
    return methods


# returns a list of all methods in a class
def get_methods_in_clazz(clazz):
    methods = map(lambda method: method, clazz['methods'])
    return methods


# returns a list of all blocks in a file
def get_code_blocks(response):
    methods = get_methods(response)
    method_blocks = map(lambda class_methods: map(lambda m: m['codeBlock'], class_methods), methods)
    return method_blocks


# return a list of boolean for each class, bool = class is access_modifier (public, protected, ..)
def get_clazzes_is_access_modifier(response, access_modifier):
    classes = get_classes(response)
    is_access_modifier_by_clazz = map(lambda clazz: clazz[access_modifier], classes)
    return is_access_modifier_by_clazz
