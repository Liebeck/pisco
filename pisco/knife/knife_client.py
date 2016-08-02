import requests
import os

KNIFE_URL = 'http://'+ ':'.join([
    os.environ['KNIFE_PORT_4567_TCP_ADDR'],
    os.environ['KNIFE_PORT_4567_TCP_PORT']])


class KnifeClient:
    def __init__(self, url=KNIFE_URL):
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
