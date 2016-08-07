def response_to_classes(response):
    return response['classes'] if response else []


def response_to_methods(response):
    return map(lambda clazz: clazz['methods'], response_to_classes(response))
