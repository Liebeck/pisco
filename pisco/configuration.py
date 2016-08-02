import logging

logger = logging.getLogger(__name__)


class Configuration():

    def __init__(self):
        self.recognizer_registry = {}
        self.dataset_registry = {}
        self.feature_registry = {}

    def feature(self, name, **args):
        logger.debug('Register feature {}, opt={}'.format(name, args))

        def decorator(f):
            if name in self.feature_registry.keys():
                raise ValueError(
                    'The feature {} is already registered. Please use another name!'.format(name))

            def wrapper():
                return f(**args)
            self.feature_registry[name] = wrapper
            return f
        return decorator

    def get_feature(self, name):
        builder = self.feature_registry.get(name)
        if builder:
            return builder()
        else:
            raise ValueError("Feature not found: {}".format(name))

    def get_feature_names(self):
        return self.feature_registry.keys()

    def recognizer(self, name, **args):
        logger.debug('Register recognizer {}, opt={}'.format(name, args))

        def decorator(f):
            if name in self.recognizer_registry.keys():
                raise ValueError(
                    'The recognizer {} is already registered. Please use another name!'.format(name))

            def wrapper():
                return f(**args)
            self.recognizer_registry[name] = wrapper
            return f
        return decorator

    def get_recognizer(self, name):
        builder = self.recognizer_registry.get(name)
        if builder:
            return builder()
        else:
            raise ValueError("Recognizer not found: {}".format(name))

    def get_recognizer_names(self):
        return self.recognizer_registry.keys()

    def dataset(self, name, **args):
        logger.debug('Register dataset {}, opt={}'.format(name, args))

        def decorator(f):
            if name in self.dataset_registry.keys():
                raise ValueError(
                    'The dataset {} is already registered. Please use another name!'.format(name))

            def wrapper():
                return f(**args)
            self.dataset_registry[name] = wrapper
            return f
        return decorator

    def get_dataset(self, name):
        builder = self.dataset_registry.get(name)
        if builder:
            return builder()
        else:
            raise ValueError("Dataset not found: {}".format(name))

    def get_dataset_names(self):
        return self.dataset_registry.keys()
