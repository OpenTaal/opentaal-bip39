for i in `cat existing-files.txt`; do
    wget https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/$i -O $i
done
