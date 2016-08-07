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
        for clazz in response['classes']:
            clazzes.append(clazz)
    return clazzes


def methods(sections):
    methods = []
    clazzes = classes(sections)
    for clazz in clazzes:
        m = []
        for method in clazz['methods']:
            m.append(method)
        methods.append(m)
    return methods
