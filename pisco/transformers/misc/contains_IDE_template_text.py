from pisco.transformers.helpers import extract_sections
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build():
    pipeline = Pipeline([('transformer',
                          ContainsIDETemplateText())])
    return ('contains_ide_template_text', pipeline)


def param_grid():
    return {}


class ContainsIDETemplateText(BaseEstimator):
    """Returns a boolean indicating whether is default text from an IDE is present
    """

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        sections = extract_sections(raw_submission)
        if sections is None:
            return [0]
        else:
            section_stats = map(lambda x: self.__transform(x), sections)
            return [max(section_stats)]

    def __transform(self, section):
        indicators = ("To change this license header, choose License Headers in Project Properties.",
                      "To change this template file, choose Tools | Templates")
        if any(indicator in section for indicator in indicators):
            return 1
        else:
            return 0
