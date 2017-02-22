import csv
import json
from collections import OrderedDict

import numpy as np

import pisco.recognizers.linear_regression as linear_regression
import pisco.recognizers.nearest_neighbors_regressor as nearest_neighbor
import pisco.transformers.misc.contains_IDE_template_text as contains_IDE_template_text  # noqa
import pisco.transformers.misc.number_of_empty_classes as number_of_empty_classes  # noqa
import pisco.transformers.misc.ratio_of_unparsable_sections as ratio_of_unparsable_sections  # noqa
import pisco.transformers.structure.comment_length as comment_length  # noqa
import pisco.transformers.structure.cyclomatic_complexity as cyclomatic_complexity  # noqa
import pisco.transformers.structure.duplicate_code_measure as duplicate_code_measure  # noqa
import pisco.transformers.structure.length_of_methods as length_of_methods  # noqa
import pisco.transformers.structure.number_of_classes as number_of_classes  # noqa
import pisco.transformers.structure.number_of_fields as number_of_fields  # noqa
import pisco.transformers.structure.number_of_local_variables_in_methods as number_of_local_variables_in_methods  # noqa
import pisco.transformers.structure.number_of_method_parameters as number_of_method_parameters  # noqa
import pisco.transformers.structure.number_of_methods as number_of_methods  # noqa
import pisco.transformers.structure.ratio_of_external_libraries as ratio_of_external_libraries  # noqa
import pisco.transformers.style.length_of_field_names as length_of_field_names  # noqa
import pisco.transformers.style.length_of_local_variable_names_in_methods as length_of_local_variable_names_in_methods  # noqa
import pisco.transformers.style.length_of_method_names as length_of_method_names  # noqa
import pisco.transformers.style.length_of_method_parameter_names as length_of_method_parameter_names  # noqa
import pisco.transformers.style.number_of_comments as number_of_comments_per_class  # noqa
from pisco.loaders.plain_loader import load
from pisco.pipeline.pipeline import pipeline

TRANSFORMERS = {'number_of_methods': number_of_methods,
                'length_of_methods': length_of_methods,
                'number_of_comments_per_class': number_of_comments_per_class,
                'ratio_of_external_libraries': ratio_of_external_libraries,
                'number_of_method_parameters': number_of_method_parameters,  # noqa
                'length_of_method_parameter_names': length_of_method_parameter_names,  # noqa
                'length_of_method_names': length_of_method_names,
                'number_of_empty_classes': number_of_empty_classes,
                'ratio_of_unparsable_sections': ratio_of_unparsable_sections,
                'contains_IDE_template_text': contains_IDE_template_text,
                'number_of_fields': number_of_fields,
                'length_of_field_names': length_of_field_names,
                'number_of_local_variables_in_methods': number_of_local_variables_in_methods,  # noqa
                'length_of_local_variable_names_in_methods': length_of_local_variable_names_in_methods,  # noqa
                'duplicate_code_measure': duplicate_code_measure,
                'comment_length': comment_length,
                'number_of_classes': number_of_classes,
                'cyclomatic_complexity': cyclomatic_complexity}

RECOGNIZERS = {'Linear Regression': linear_regression,
               'Nearest Neighbor': nearest_neighbor}


def build_recognizer(configfile):
    """Parses the recognizer from a config file and returns
    an instance of the recognizer

    Args:
        configfile: JSON config file
    Returns:
        An instance of the recognizer
    """
    nfeatures = num_features(configfile)
    recognizer_params = {}
    with open(configfile) as data_file:
        data = json.load(data_file)
        best_params = data[str(nfeatures) + 'features']['best_params']
        recognizer_name = data['recognizer_name']
        for k, v in best_params.iteritems():
            splits = k.split('__')
            if splits[0] == 'recognizer':
                if v == u'default':
                    recognizer_params = {}
                else:
                    param_name = splits[-1]
                    recognizer_params[str(param_name)] = v
        return RECOGNIZERS[recognizer_name].build(**recognizer_params)


def build_features(configfile):
    """Parses the features from a config file and returns
    instances of the features

    Args:
        configfile: JSON config file
    Returns:
        Instances of the features
    """
    nfeatures = num_features(configfile)
    features = {}
    with open(configfile) as data_file:
        data = json.load(data_file)
        best_params = data[str(nfeatures) + 'features']['best_params']
        for k, v in best_params.iteritems():
            splits = k.split('__')
            if splits[0] == 'union':
                transformer_name = splits[1]
                if v == u'default':
                    features[transformer_name] = {}
                else:
                    param_name = splits[-1]
                    if transformer_name not in features:
                        features[transformer_name] = {}
                    features[transformer_name][str(param_name)] = str(v)
    feature_instances = []
    for k, v in features.iteritems():
        if not v:
            feature_instances.append(TRANSFORMERS[k].build(**v))
        else:
            feature_instances.append(TRANSFORMERS[k].build())
    return feature_instances


def num_features(configfile):
    """Parses the number of features from a JSON config file

    Args:
        configfile: JSON config file
    Returns:
        Number of features
    """
    with open(configfile) as data_file:
        data = json.load(data_file)
        first_key = None
        for key in data.keys():
            if key[0].isdigit():
                first_key = key
                break
        return int(first_key.replace("features", ""))


def predict(configs):
    """Given a configuration dictionary, predicts
    the labels for the test data

    Args:
        configfile: dictionary with dimensions as
          keys and values as path to config files
    Returns:
        Predictions of test data
    """
    predictions = OrderedDict()
    for dimension, configfile in configs.iteritems():
        X_train, Y_train = load(labels=[dimension])
        features = build_features(configs[dimension])
        recognizer = build_recognizer(configs[dimension])
        nfeatures = num_features(configs[dimension])
        p = pipeline(transformers=features,
                     recognizer=recognizer,
                     number_of_features=nfeatures)
        p.fit(X_train, Y_train)
        scores = p.named_steps['feature_selection'].scores_
        top_ranked_features = sorted(enumerate(scores), key=lambda x: x[1],
                                     reverse=True)[:nfeatures]
        top_ranked_features_indices = map(list, zip(*top_ranked_features))[0]
        feature_names = p.named_steps['union'].get_feature_names()
        print('*'*30)
        print("Selected {} Features for Dimension".format(nfeatures),
              dimension)
        print('*'*30)
        for feature in np.asarray(feature_names)[top_ranked_features_indices]:
                    print feature
        X_test, ids = load(corpus_path='data/test', labels=dimension,
                           truth_file=None, return_ids=True)
        Y_pred = p.predict(X_test)
        for y_pred, _id in zip(Y_pred, ids):
            if not predictions.get(_id, None):
                predictions[_id] = OrderedDict()
            predictions[_id][dimension] = y_pred
    return predictions


def write_predictions(predictions, filepath):
    """Writes predictions as a csv file

    Args:
        predictions: predicted values for test data
        filepath: path to the output file
    """
    with open(filepath, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        header = ['id'] + predictions[predictions.keys()[0]].keys()
        writer.writerow(header)
        for _id, values in predictions.iteritems():
            ps = []
            for dimension, value in values.iteritems():
                ps.append(values[dimension])
            writer.writerow([_id] + ps)
