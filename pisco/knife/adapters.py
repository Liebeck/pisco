from pisco import client


def classes(section):
    response = client.extract(section)
    if response:
        return response['classes']
    else:
        return None


def methods(section):
    return map(lambda clazz: _methods(clazz), classes(section))


def method_blocks(section):
    return map(lambda c: _method_blocks(c), classes(section))


def comments(section, types=['block', 'line']):
    return map(lambda clazz: _comments(clazz, types), classes(section))


def _methods(clazz):
    if clazz:
        return clazz['methods']
    else:
        None


def _method_blocks(clazz):
    return map(lambda m: m.get('sourceCode', None), _methods(clazz))


def _comments(clazz, types=['block', 'line']):
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
