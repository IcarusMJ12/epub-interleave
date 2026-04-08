#!/usr/bin/env python

"""
Breaks a text into sentences, each one on a new line.  Paragraphs are
double-spaced.
"""

import spacy

PARAGRAPH_SEP = '\n\n'
MODEL_XX = spacy.load('xx_sent_ud_sm')


def txt2paragraphs(txt):
    for p in txt.split(PARAGRAPH_SEP):
      yield MODEL_XX(''.join(p.strip().split('\n'))).sents


def main():
  from sys import stdin

  txt = stdin.read()
  for p in txt2paragraphs(txt):
    for s in p:
      print(s)
    print('')


if __name__ == '__main__':
  main()
