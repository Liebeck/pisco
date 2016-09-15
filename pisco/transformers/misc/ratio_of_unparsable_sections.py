from pisco.transformers.helpers import extract_sections
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build():
    pipeline = Pipeline([('transformer',
                          RatioOfKnifeUnparsableSection())])
    return ('ratio_of_knife_unparsable_sections', pipeline)


def param_grid():
    return {'union__ratio_of_knife_unparsable_sections__transformer':
            ['default']}

class RatioOfKnifeUnparsableSection(BaseEstimator):
    """Returns a ratio of sections that are unparsable by knife.
    1 is the highest value which indicates that no section is parsable
    """

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        sections = extract_sections(raw_submission)
        if sections is None:
            return [1]
        else:
            section_stats = map(lambda x: self.__transform(x),
                                sections)  # Be aware that a class might contain no functions
            return [sum(section_stats) / float(len(section_stats))]

    def __transform(self, section):
        clazzes = adapter.classes(section)
        if clazzes:
            return 0
        else:
            return 1
