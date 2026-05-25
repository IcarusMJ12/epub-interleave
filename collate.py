#!/usr/bin/env python

"""
Collates two translations of a text into an interleaved sentence-by-sentence
form and outputs to stdout.
"""

from pickle import load


def score(alignment):
  if not (len(alignment.src_sentences) and len(alignment.tgt_sentences)):
    return 100
  return min(alignment.score, 1) * 100


def collate(template, res):
  body = [f'''
    <div class="sent">
      <div class="bar" style="width: {score(a)}%"></div>
      <p>{''.join(a.src_sentences)}</p>
      <p>{''.join(a.tgt_sentences)}</p>
    </div>''' for a in res.alignments]
  return template.replace('$body', ''.join(body))


def main():
  from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

  parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                          description=__doc__)
  parser.add_argument('--template', '-t', default='template.html',
                      help='html template to use (must contain `$body`)')
  parser.add_argument('pickle', help='A pickled `SentAlignResult` file')

  args = parser.parse_args()

  with open(args.pickle, 'rb') as f:
    res = load(f)

  with open(args.template, 'r') as f:
    template = f.read()

  print(collate(template, res))


if __name__ == '__main__':
  main()
