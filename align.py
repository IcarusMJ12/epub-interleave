#!/usr/bin/env python

"""
Aligns two translations of a text using `sentalign` into a pickled
`SentAlignResult`.
"""

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from pickle import dump


def main():
  parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                          description=__doc__)
  parser.add_argument('--model', '-m', default='google/embeddinggemma-300m',
                      help='embedding language model')
  parser.add_argument('input', nargs=2, help='text files to collate')
  parser.add_argument('output', nargs='?', default='out.pickle',
                      help='output pickle file name')
  args = parser.parse_args()

  with open(args.input[0], 'r') as f:
    txt1 = f.read().split('\n')
  with open(args.input[1], 'r') as f:
    txt2 = f.read().split('\n')
  print('Loading model...')
  from sentence_transformers import SentenceTransformer
  model = SentenceTransformer(args.model)

  from sentalign import sentalign

  with open(args.output, 'wb') as f:
    print('Aligning sentences, this may take a while...')
    dump(sentalign(txt1, txt2, model, alignment_max_size=4), f)


if __name__ == '__main__':
  main()
