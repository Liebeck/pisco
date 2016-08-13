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


def comments(sections, types=['block']):
    types_map = {'block': 'BlockComment',
                 'line': 'LineComment',
                 'javadoc': 'JavadocComment'}
    new_types = map(lambda t: types_map[t], types)
    css = classes(sections)
    comments = []
    for cs in css:
        a = []
        for t in types:
            a.append([])
        if cs:
            class_comments = cs['comments']
            for cc in class_comments:
                if cc['type'] in new_types:
                    idx = types_map.keys()[types_map.values().index(
                        cc['type'])]
                    a[types.index(idx)].append(cc['content'])
                else:
                    a.append(None)
        a = [[], [], []]
        comments.append(a)
    return comments
