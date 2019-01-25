#!/bin/sh

pr -l 69 -w 90 -S" | " --columns=2 spyder-keys.rst > tmp.txt
recode utf-8..latin1 < tmp.txt > tmp2.txt
enscript -B tmp2.txt -o spyder-keys.ps
psselect -p1-4 spyder-keys.ps tmp.ps
mv tmp.ps spyder-keys.ps
ps2pdf  spyder-keys.ps spyder-keys.pdf
rm -f tmp2.txt tmp.txt tmp.ps spyder-keys.ps
