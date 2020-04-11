set -e

if [ ! -e ../downloads ]; then
	mkdir ../downloads
fi
cd ../downloads

wget --quiet https://github.com/bitcoin/bips/archive/master.zip
if [ -e bips-master ]; then
	rm -rf bips-master
fi
unzip -q master.zip
rm -f master.zip
cd bips-master
rm -rf $(ls|grep -v 0039) .travis.yml
cd ..

if [ -e correct-words-with-frequency.tsv ]; then
	rm -f correct-words-with-frequency.tsv
fi
scp -q zaph:database-tools/correct-	words-with-frequency.tsv .

cd ../tools
