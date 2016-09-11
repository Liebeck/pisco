from pisco.transformers.helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build(stat='mean'):
    pipeline = Pipeline([('transformer',
                          RatioOfKnifeUnparsableSection(stat=stat))])
    return ('ratio_of_knife_unparsable_section', pipeline)


def param_grid():
    return {}


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
            print "sections is None"
            return [1]
        else:
            section_stats = map(lambda x: self.__transform(x),
                                sections)  # Be aware that a class might contain no functions
            print section_stats
            return [sum(section_stats) / float(len(section_stats))]

    def __transform(self, section):
        clazzes = adapter.classes(section)
        if clazzes:
            print "clazzes is None"
            return 0
        else:
            print "clazzes is not None"
            return 1
