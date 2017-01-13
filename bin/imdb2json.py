#!/usr/bin/python3

import json
import multiprocessing
import os
import os.path
import re

import gargparse
from gargparse import ARGS
import nltokeniz


POS = 'pos'
NEG = 'neg'

TRAIN = 'train'
TEST = 'test'


gargparse.add_argument('input_dirname')
gargparse.add_argument('output_dirname')


def get_files(dirname):
    return [os.path.join(dirname, filename)
            for filename in os.listdir(dirname)]


def convert_file(filename):
    binary_class = os.path.basename(os.path.dirname(filename))
    assert binary_class in {POS, NEG}

    with open(filename) as phile:
        return {
            'filename': filename,
            'document': nltokeniz.tokenize(phile.read()),
            'label': {
                'binary': 1 if binary_class == POS else 0,
                'multi': int(re.search(r'_([0-9]+)\.txt$', filename).group(1)),
            },
        }


def convert_filename(filename):
    return (('pos' if 'pos/' in filename else 'neg')
            + '_'
            + re.match(r'(.*)_[0-9]+$',
                       os.path.splitext(os.path.basename(filename))[0]).group(1)
            + '.json')


def write_json_file(filename):
    with open(os.path.join(ARGS.output_dirname,
                           ('train' if 'train/' in filename else 'test'),
                           convert_filename(filename)),
              'w') as phile:
        json.dump(convert_file(filename),
                  phile,
                  ensure_ascii=False,
                  indent='\t')


def main():
    for data_use in [TRAIN, TEST]:
        os.makedirs(os.path.join(ARGS.output_dirname, data_use), exist_ok=True)

        for binary_class in [POS, NEG]:
            multiprocessing.Pool().map(
                write_json_file,
                get_files(os.path.join(ARGS.input_dirname,
                                       data_use,
                                       binary_class)))


if __name__ == '__main__':
    main()
