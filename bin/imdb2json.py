#!/usr/bin/python3

import argparse
import json
import os
import os.path
import re


POS = 'pos'
NEG = 'neg'

TRAIN = 'train'
TEST = 'test'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dirname')
    parser.add_argument('output_dirname')
    return parser.parse_args()


def get_files(dirname):
    return [os.path.join(dirname, filename)
            for filename in os.listdir(dirname)]


def convert_file(filename):
    binary_class = os.path.basename(os.path.dirname(filename))
    assert binary_class in {POS, NEG}

    with open(filename) as phile:
        return {
            'filename': filename,
            'document': phile.read().split(),
            'label': {
                'binary': 1 if binary_class == POS else 0,
                'multi': int(re.search(r'_([0-9]+)\.txt$', filename).group(1)),
            },
        }


def convert_filename(filename, binary_class):
    return (binary_class
            + '_'
            + re.match(r'(.*)_[0-9]+$', os.path.splitext(filename)[0]).group(1)
            + '.json')


def main():
    args = get_args()

    for data_use in [TRAIN, TEST]:
        for binary_class in [POS, NEG]:
            for filename in get_files(os.path.join(args.input_dirname,
                                                   data_use,
                                                   binary_class)):
                os.makedirs(os.path.join(args.output_dirname, data_use),
                            exist_ok=True)

                with open(
                        os.path.join(
                            args.output_dirname,
                            data_use,
                            convert_filename(os.path.basename(filename),
                                             binary_class)),
                        'w') as phile:
                    json.dump(convert_file(filename),
                              phile,
                              ensure_ascii=False,
                              indent='\t')


if __name__ == '__main__':
    main()
