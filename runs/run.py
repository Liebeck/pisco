#!/usr/bin/env python
from helper import predict, write_predictions
import argparse
import os


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Submission Script')
    argparser.add_argument('-r', '--run_folder', type=str, required=True,
                           help='Path to a run folder')

    args = argparser.parse_args()
    run_folder = args.run_folder

    neuroticism = 'configs/neuroticism.json'
    extroversion = 'configs/extroversion.json'
    openness = 'configs/openness.json'
    agreeableness = 'configs/agreeableness.json'
    conscientiousness = 'configs/conscientiousness.json'

    CONFIGS = {'neuroticism':
               os.path.join(run_folder, neuroticism),
               'extroversion':
               os.path.join(run_folder, extroversion),
               'openness':
               os.path.join(run_folder, openness),
               'agreeableness':
               os.path.join(run_folder, agreeableness),
               'conscientiousness':
               os.path.join(run_folder, conscientiousness)}

    outputfile_name = 'results.txt'

    predictions = predict(CONFIGS)
    write_predictions(predictions, os.path.join(run_folder, outputfile_name))
