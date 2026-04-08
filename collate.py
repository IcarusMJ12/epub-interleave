#!/usr/bin/env python

"""
Collate two translations of a text into an interleaved sentence-by-sentence
form.
"""

from pickle import load


def score(alignment):
  if not (len(alignment.src_sentences) and len(alignment.tgt_sentences)):
    return 100
  return min(alignment.score, 1) * 100


def collate(res):
  with open('template.html', 'r') as f:
    html = f.read()
  body = [f'''
    <div class="sent">
      <div class="bar" style="width: {score(a)}%"></div>
      <p>{''.join(a.src_sentences)}</p>
      <p>{''.join(a.tgt_sentences)}</p>
    </div>''' for a in res.alignments]
  return html.replace('$body', ''.join(body))


def main():
  from argparse import ArgumentParser

  parser = ArgumentParser(description=__doc__)
  parser.add_argument('pickle', help='A pickled `SentAlignResult` file')

  args = parser.parse_args()
  with open(args.pickle, 'rb') as f:
    res = load(f)

  print(collate(res))



if __name__ == '__main__':
  main()
