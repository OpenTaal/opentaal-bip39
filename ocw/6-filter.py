#!/usr/bin/env python3

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' )

def illegal_character(word):
	for character in word:
		if character not in alphabet:
			return True
	return False

# ei ij
# c k
# c s
# e u

existing = set()
# ./3-download.sh
for path in open('existing-files.txt'):
	for line in open(path[:-1]):
		word = line[:-1]
		existing.add(word)
for path in open('word-list-files.txt'):
	try:
		for line in open(path[:-1]):
			word = line[:-1]
			if len(word) < 5 or len(word) > 8:
				continue
			if illegal_character(word):
				continue
			existing.add(word)
	except UnicodeDecodeError:
		for line in open(path[:-1], encoding='ISO-8859-1'):
			word = line[:-1]
			if len(word) < 5 or len(word) > 8:
				continue
			if illegal_character(word):
				continue
			existing.add(word)

words = set()
for line in open('stcrt-2015-35790.txt'):
	word = line[:-1]
	if len(word) < 5 or len(word) > 8:
		continue
	if word in existing:
		continue
	if illegal_character(word):
		continue
	words.add(word)
		
print(len(words))
	
out = open('dutch.txt', 'w')
for word in sorted(words):
	out.write('{}\n'.format(word))
