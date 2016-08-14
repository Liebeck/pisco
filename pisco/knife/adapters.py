from pisco import client


def classes(sections):
    return map(lambda section: _classes(section), sections)


def _classes(section):
    response = client.extract(section)
    if response:
        return response['classes']
    else:
        return None


def methods(section):
    return map(lambda clazz: _methods(clazz), _classes(section))


def _methods(clazz):
    if clazz:
        return clazz['methods']
    else:
        None


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


def comments(section, types=['block', 'line']):
    a = map(lambda clazz: __comments(clazz, types), _classes(section))
    return a


def __comments(clazz, types=['block', 'line']):
    mapping = {u'BlockComment': u'block',
               u'LineComment': u'line',
               u'JavadocComment': u'javadoc'}
    comments_ = dict()
    for t in types:
        comments_[t] = []
    for c in clazz['comments']:
            comment_type = c[u'type']
            comments_[mapping[comment_type]].append(c['content'])
    return comments_
