# Dutch words for BIP 39

This is the Dutch contribution for BIP: 39, titled Mnemonic code for generating
deterministic keys. See https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki
and https://github.com/bitcoin/bips/blob/master/bip-0039/bip-0039-wordlists.md .
The selection criteria used are discussed step by step below.

## Number of words

An exact number of 2048 words must be selected.

## Word characters

Words may consist only of lower case characters `a` to `z`.

## Word length

According to https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki we
choose a minimum word length of four characters. According to the output of
`./analyse.sh` in `tools`, a maximum word length of eight is chosen.

## Unique words

At least the first four letters of each word must be unique.

## Known words

Words will be preferred based on their word frequency from quality corpora.

## Word types

Words with only the following POS-tags are considered:
*
*
*

Words that have multiple POS-tags are ignored as to avoid unambiguous word
meaning. TODO maybe not

## Avoiding words

Words which are very similar in spelling or sound should be avoided. TODO




## Word sorting

By the type of characters found in the selected words, a normal sorting can be
used. No special localized sorting is needed.
