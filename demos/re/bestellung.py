# bestellung.py

import re

re_whitespace = re.compile('^\s*$')
re_comment = re.compile('^#.*$')
re_line = re.compile('^\s*(\d+)\s+(\d+)\s+(\S[\S\s]+)\;\s+(\S+)\s+(\S+)')

FILE = "bestellung.txt"

def main():
    fd = open(FILE, 'r')
    summe = 0.0
    while 1:
        line = fd.readline()
        if not line:
            break
        if re_whitespace.match(line):
            pass
        elif re_comment.match(line):
            print(line, end=" ")
        else:
            mobj = re_line.match(line)
            print(line, end=" ")
            (pos, anzahl, beschreibung, bestnr, preis) = mobj.groups()
            summe = summe + int(anzahl) * float(preis)
    fd.close()
    print("Summe = %.02f" % summe, "Euro")
    
if __name__ == "__main__":
    main()
