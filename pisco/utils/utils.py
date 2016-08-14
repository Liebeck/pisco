import sys


def extract_classes(X):
    list_class_list = []
    for x in X:
        class_list = x.split(u"<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>\r")
        list_class_list.append(class_list)
    return list_class_list
