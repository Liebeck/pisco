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
