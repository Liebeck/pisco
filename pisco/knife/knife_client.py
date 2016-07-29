import requests
import os


class KnifeClient:
    # TODO: Extract the hard-coded server to a config file
    def __init__(self, url='http://0.0.0.0:4567/'):
        self.url = url

    def extract_method_blocks(self, clazz=None):
        r = requests.post(os.path.join(self.url, 'method/blocks'),
                          data={'class': clazz})
        return r.json()['methodBlocks']
