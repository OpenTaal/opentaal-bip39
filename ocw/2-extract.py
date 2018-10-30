#!/usr/bin/env python3

from operator import itemgetter
from os.path import isfile
from xml.etree import ElementTree
from pprint import pprint
from _operator import pos

def histogram(data, name):
	print(name)
	for value, count in sorted(data.items(), key=itemgetter(1)):
		print('{}\t{}'.format(count, value)) 

# https://zoek.officielebekendmakingen.nl/stcrt-2015-35790.html

filename = 'stcrt-2015-35790.xml'
if not isfile(filename):
	print('ERROR: Missing file {}'.format(filename))
	exit(1)

words = set()
characters = []
root = ElementTree.parse(filename).getroot()
for al in root.findall('./staatscourant/circulaire/bijlage/al-groep/*'):
	words.add(al.text)

out = open('stcrt-2015-35790.txt', 'w')
for word in sorted(words):
	out.write('{}\n'.format(word))

# 
# #histogram(detailed_characters, 'detailed_characters')
# #histogram(characters, 'characters')
# #histogram(detailed_part_of_speechs, 'detailed_part_of_speechs')
# #histogram(part_of_speechs, 'part_of_speechs')
# 
# aff = open('../tlh_Latn.aff', 'w')
# aff.write('# Author: Pander <pander@users.sourceforge.net>\n')
# aff.write('# License: Apache License 2.0\n')
# aff.write('# Version: 0.1\n')
# aff.write('# Date: 2018-02-23\n')
# aff.write('SET UTF-8\n')
# aff.write('TRY {}\n'.format(''.join(alphabet)))
# # support apostrophe TODO Note below that WORDCHARS are being used! Discuss for Nuspell.
# aff.write('WORDCHARS {}’\n'.format(''.join(alphabet)))
# aff.write('ICONV 1\n')
# aff.write("ICONV ’ '\n")
# # support QEWRTY and AZERTY keyboards
# aff.write('KEY qwertyuiop|asdfghjkl|zxcvbnm|qawsedrftgyhujikolp|azsxdcfvgbhnjmk|aze|qsd|lm|wx|aqz|qws|\n')
# # suffixes
# for flag, affixes in sorted(suffixes.items()):
# 	aff.write('SFX {} Y {}\n'.format(flag, len(affixes)))
# 	for affix in sorted(affixes):
# 		aff.write('SFX {} 0 {} .\n'.format(flag, affix))
# # prefixes
# for flag, affixes in sorted(prefixes.items()):
# 	aff.write('PFX {} Y {}\n'.format(flag, len(affixes)))
# 	for affix in sorted(affixes):
# 		aff.write('PFX {} 0 {} .\n'.format(flag, affix))
# 
# dic = open('../tlh_Latn.dic', 'w')
# dic.write('{}\n'.format(len(dict)))
# for word, flags in sorted(dict.items()):
# 	if flags:
# 		dic.write('{}/{}\n'.format(word, ''.join(flags)))
# 	else:
# 		dic.write('{}\n'.format(word))
# 
# tst = open('../klingon-latin', 'w')
# for word in sorted(words):
# 	tst.write('{}\n'.format(word))
# 
# tst = open('../tests', 'w')
# for word in sorted(tests):
# 	tst.write('{}\n'.format(word))
