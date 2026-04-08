#!/usr/bin/env python
"""
Aligns two translations of a text using `sentalign` into a pickled
`SentAlignResult`.
"""

from pickle import dump

from sentence_transformers import SentenceTransformer

from sentalign import sentalign

MODEL = SentenceTransformer('google/embeddinggemma-300m')


def main():
  from argparse import ArgumentParser

  parser = ArgumentParser(description=__doc__)
  parser.add_argument('input', nargs=2, help='Text files to collate.')
  parser.add_argument('output', default='out.pickle',
                      help='Output pickle file name')
  args = parser.parse_args()

  with open(args.input[0], 'r') as f:
    txt1 = f.read().split('\n')
  with open(args.input[1], 'r') as f:
    txt2 = f.read().split('\n')

  with open(args.output, 'wb') as f:
    print('Aligning sentences, this may take a while...')
    dump(sentalign(txt1, txt2, MODEL, alignment_max_size=4), f)


if __name__ == '__main__':
  main()
