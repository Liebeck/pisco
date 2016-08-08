from pisco import client


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
    for mm in methods_:
        m = []
        for t in mm:
            if t:
                m.append(t['sourceCode'])
            else:
                m.append(None)
        method_blocks.append(m)
    return method_blocks
