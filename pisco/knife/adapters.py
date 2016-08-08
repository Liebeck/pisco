import logging
from pisco import client


def response_to_classes(response):
    return response['classes'] if response else []


def response_to_methods(response):
    classes = response_to_classes(response)
    logging.info(classes)
    return map(lambda clazz: clazz['methods'], response_to_classes(response))


def classes(sections):
    clazzes = []
    for section in sections:
        response = client.extract(section)
        if response:
            for clazz in response['classes']:
                clazzes.append(clazz)
        else:
            clazzes.append(None)
    return clazzes


def methods(sections):
    methods = []
    clazzes = classes(sections)
    for clazz in clazzes:
        m = []
        if clazz:
            for method in clazz['methods']:
                m.append(method)
        else:
            m.append(None)
        methods.append(m)
    return methods


def method_blocks(sections):
    methods_ = methods(sections)
    method_blocks = []
    for m in methods_:
        method_blocks.append(m['codeBlock'])
    return method_blocks
