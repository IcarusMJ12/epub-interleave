#!/usr/bin/env python

"""
Checks provides XML (or HTML) file for invalid characters.
"""

RESTRICTED = [(0x1, 0x8), (0xB, 0xC), (0xE, 0x1F), (0x7F, 0x84), (0x86, 0x9F)]


def is_restricted(c):
  for l, u in RESTRICTED:
    if l <= ord(c) <= u:
      return True
  return False


def check(lines):
  invalid = []
  for idx, line in enumerate(lines):
    if any(is_restricted(c) for c in line):
      yield (idx, line)


def main():
  from argparse import ArgumentParser

  parser = ArgumentParser(description=__doc__)
  parser.add_argument('xml', help='XML (or HTML) file to check for invalid '\
                                  'characters.')
  args = parser.parse_args()
  with open(args.xml, 'r') as f:
    lines = f.readlines()
  found = False
  for idx, line in check(lines):
    found = True
    print(f'{idx + 1}: {line}')
  if not found:
    print('All good!')


if __name__ == '__main__':
  main()
