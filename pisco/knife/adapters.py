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


def method_blocks(section):
    return map(lambda c: _method_blocks(c), _classes(section))


def _method_blocks(clazz):
    methods_ = _methods(clazz)
    return map(lambda m: m.get('sourceCode', None), methods_)


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
