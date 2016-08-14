from pisco import client


def classes(section):
    """Extracts all classes from a section.

    Args:
        section: string content of a code section
    Returns:
        list consisting of dictionaries representing a class
    """
    response = client.extract(section)
    if response:
        return response['classes']
    else:
        return None


def methods(section):
    """Extracts all methods from a section. Note that a section
    can consist of multiple classes. So the result will be a list
    of lists. For example if we have a section with two classes
    and each class consists of two methods the result will be of
    the following form: [[m1,m2], [m3,m4]]

    Args:
        section: string content of a code section
    Returns:
        list of list of methods
    """
    return map(lambda clazz: _methods(clazz), classes(section))


def method_blocks(section):
    """Extracts all classes from a section.

    Args:
        section: string content of a code section
    Returns:
        list consisting of dictionaries representing a class
    """
    return map(lambda c: _method_blocks(c), classes(section))


def comments(section, types=['block', 'line']):
    """Extracts all comments from a section. Comments are
    represented as a dictionary with the given types as keys.
    For example if we have two classes, one with two block comments
    and one line comments and the other one without any comments
    the reslult we be as follows: [[{'block':'', 'line':''}], [{}]]

    Args:
        section: string content of a code section
        types: types of comments to be extracted
    Returns:
        list of list of methods
    """
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
