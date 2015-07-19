./getmeaning.py $1
sed -i .bak -e 's/\\\\/\\\\ \\hline/g; s/{ll}/{\\linewidth}{c|C}/g; s/{tabular}/{tabulary}/g' meaning_$1 
rm meaning_$1.bak
