#!/usr/bin/env python

"""
Collate two translations of a text into an interleaved sentence-by-sentence
form.
"""

from sentence_transformers import SentenceTransformer, util

PARAGRAPH_SEP = '\n\n'
MODEL = SentenceTransformer('google/embeddinggemma-300m')
CMP_THRESHOLD = 0.5

embeds = {}

def embed(sent):
  if sent not in embeds.keys():
    embeds[sent] = MODEL.encode(sent, convert_to_tensor=True)
  return embeds[sent]


def compare(sent1, sent2):
  return util.pytorch_cos_sim(embed(sent1), embed(sent2))[0][0]


def split_text(txt):
  return [p.split('\n') for p in txt.split(PARAGRAPH_SEP)]


def collate(txt1, txt2):
  txt1, txt2 = split_text(txt1), split_text(txt2)
  len1, len2 = [len(p) for p in txt1], [len(p) for p in txt2]

  i1, i2 = 0, 0
  # find offsets of the first non-trivial (>1 sentence) paragraph
  while len1[i1] == 1:
    i1 += 1
  while len2[i2] == 1:
    i2 += 1
  # if mismatched, find one matching the longest length
  while len1[i1] > len2[i2]:
    i2 += 1
  while len2[i2] > len1[i1]:
    i1 += 1

  #TODO: collate backwards from first proper paragraph

  while len1[i1] == len2[i2]:
    p1, p2 = txt1[i1], txt2[i2]
    j = 0
    while j < len(p1):
      print(f'{p1[j]}\n{p2[j]}\n{compare(embed(p1[j]), embed(p2[j]))}\n')
      j += 1
    i1 += 1
    i2 += 1
    print('\n')

  print(f'{len1[i1]} {len2[i2]}')


def main():
  from argparse import ArgumentParser

  parser = ArgumentParser(description=__doc__)
  parser.add_argument('file', nargs=2, help='Files to collate.')
  args = parser.parse_args()

  with open(args.file[0], 'r') as f:
    txt1 = f.read()
  with open(args.file[1], 'r') as f:
    txt2 = f.read()

  collate(txt1, txt2)


if __name__ == '__main__':
  main()
