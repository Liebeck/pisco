#!/usr/bin/env python
import argparse
import json
import os


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Find Best Params')
    argparser.add_argument('-f', '--folder', type=str, required=True,
                           help='Folder containing the result files')
    argparser.add_argument('-s', '--score', type=str, required=True,
                           help='Desired scoring function')
    argparser.add_argument('-r', '--recognizer', type=str, required=True,
                           help='Desired recognizer')
    argparser.add_argument('-d', '--dimension', type=str, required=True,
                           help='Desired dimension')

    args = argparser.parse_args()
    folder = args.folder
    score = args.score
    recognizer = args.recognizer
    dimension = args.dimension
    candidate_files = []
    for root, directories, files in os.walk(folder):
        for filename in files:
            splits = filename.split('_')
            d = splits[1]
            s = splits[2]
            r = splits[3]
            if d == dimension and s == score and r == recognizer:
                candidate_files.append(filename)
    score_file_map = {}
    for f in candidate_files:
        with open(os.path.join(folder, f)) as data_file:
            data = json.load(data_file)
            best_score = data[data.keys()[0]]['best_score']
            score_file_map[best_score] = f
    overall_best_score = max(best_score)
    print score_file_map[overall_best_score]
