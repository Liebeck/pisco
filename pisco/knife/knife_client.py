import requests
import os

# Todo: Workaround for travis environment variables
KNIFE_URL = 'http://' + ':'.join([
    os.getenv('KNIFE_PORT_4567_TCP_ADDR', 'Travis_default'),
    os.getenv('KNIFE_PORT_4567_TCP_PORT', 'Travis_default')])


class KnifeClient:
    def __init__(self, url=KNIFE_URL):
        self.url = url
        self.memory = {}

    def extract(self, clazz):
        if clazz not in self.memory:
            r = requests.post(os.path.join(self.url, 'extract'),
                              data={'class': clazz})
            self.memory[clazz] = r
        else:
            r = self.memory[clazz]
        if r.json()['state'] == 'OK':
            return r.json()
        else:
            return None

    # TODO: Refactor method_blocks with the new request / response model
    def method_blocks(self, clazz=None):
        r = requests.post(os.path.join(self.url, 'extract'),
                          data={'class': clazz})
        if r.json()['state'] == 'OK':
            all_methods = map(lambda clazz: clazz['methods'],
                              r.json()['classes'])
            method_blocks = map(lambda class_methods: map(
                lambda m: m['codeBlock'], class_methods), all_methods)
            return method_blocks
        else:
            return None
