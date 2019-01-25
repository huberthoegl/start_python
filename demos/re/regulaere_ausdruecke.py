# regulaere_ausdruecke.py 
# Hubert Hoegl, 2002-11-18, <Hubert.Hoegl@t-online.de>

import re

def main():
    str = 'Das Jahr 2002 geht zu Ende - danach kommt 2003.'

    # Suche nach mehreren zusammenhaengenden Ziffern
    pattern = '\d+' 
    L = re.findall(pattern, str)
    print(L)

    pattern = 'http://(\S+)/(\S+)'  # \S : alles ausser Leerzeichen
    str = 'http://www.dlr.de/index.html'
    mobj = re.match(pattern, str)
    print(mobj.groups())

    str = '1 2 3 4 5 6'
    pattern = '2|5'  # 2 oder 5
    print(re.sub(pattern, 'xxx', str))

    str = '01 Hier 02 haben 03 wir 04 Zahlen 05 als 06 Trenner'
    pattern = '\d+'
    print(re.split(pattern, str))

    str = '     Beachten Sie die Leerzeichen links und rechts.      '
    pattern = '\s*(.*\.)\s*'  # \s : Leerzeichen (' ', \t, \n, \r, \f (form feed), \v (vtab))
    mobj = re.match(pattern, str)
    print(mobj.groups())


if __name__ == "__main__":
    main()

