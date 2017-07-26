#!/usr/bin/env python

import argparse
import rmfiles2

parser = argparse.ArgumentParser(
    description='Cancella file in modo ricorsivo')
parser.add_argument(
    '-base_path',
    type=str,
    default='.',
    help='Percorso iniziale')
parser.add_argument(
    '-suffix',
    type=str,
    default='.pyc',
    help='Suffisso dei file')

args = parser.parse_args()
rmfiles2.remove_recursively(args.base_path, args.suffix)
