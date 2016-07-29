import requests
import os


class KnifeClient:
    # TODO: Extract the hard-coded server to a config file
    def __init__(self, url='http://0.0.0.0:4567/'):
        self.url = url

    def method_blocks(self, clazz=None):
        r = requests.post(os.path.join(self.url, 'extract'),
                          data={'class': clazz})
        if r.json()['state'] == 'OK':
            all_methods = map(lambda clazz: clazz['methods'],r.json()['classes'])
            method_blocks = map(lambda class_methods: map(lambda m: m['codeBlock'], class_methods),all_methods)
            return method_blocks
        else:
            return None
