#!/usr/bin/env python3

from glob import glob
from operator import itemgetter
from os.path import isdir
from sys import maxsize


if not isdir('../downloads/bips-master'):
  print('ERROR: First run ./download.sh')
  exit(1)

for name in sorted(glob('../downloads/bips-master/bip-0039/*.txt')):
  total = 0
  min = maxsize
  max = 0
  lengths = {}
  firsts = {}
  for line in open(name):
    line = line[:-1]
    total += 1
    length = len(line)
    if length < min:
      min = length
    if length > max:
      max = length
    if length in lengths:
      lengths[length] += 1
    else:
      lengths[length] = 1
    first = line[0]	
    if first in firsts:
      firsts[first] += 1
    else:
      firsts[first] = 1
  print('filename: {}'.format(name[name.rfind('/')+1:]))
  print('\tnumber of words: {}'.format(total))
  print('\tminimum word length: {}'.format(min))
  print('\tmaximum word length: {}'.format(max))
  if min == max:
    continue
  print('\tword length histogram:')
  for length, count in sorted(lengths.items()):
    print('\t{} {}'.format(length, count))
  min_first = maxsize
  for first, count in firsts.items():
    if count < min_first:
      min_first = count
  print('\tminimum first character: {}'.format(min_first))
  print('\tfirst character histogram:')
  for first, count in sorted(firsts.items(), key=itemgetter(1), reverse=True):
    print('\t{} {}'.format(first, count))
