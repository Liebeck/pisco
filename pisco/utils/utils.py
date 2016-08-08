import sys


def extract_classes(X):
    list_class_list = []
    for x in X:
        class_list = x.split(u"<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>\r")
        list_class_list.append(class_list)
    return list_class_list


def print_progress_bar(i, max, message, print_new_line=True):
    percent = float(i) / max
    # print percent
    hashes = '#' * int(round(percent * 20))
    spaces = ' ' * (20 - len(hashes))
    sys.stdout.write("\r{0}: [{1}] {2}%".format(
        message, hashes + spaces, int(round(percent * 100))))
    if print_new_line and (i == max):
        sys.stdout.write("\n")
    sys.stdout.flush()
