# http://docs.python.org/3/library/ftplib.html
# H. Hoegl, 2013-04-15 

import ftplib

FN = "nano-2.3.2.tar.gz"

ftp = ftplib.FTP("ftp.gnu.org")
ftp.login()  # anon
ftp.cwd('gnu')
ftp.retrlines('LIST')
ftp.cwd('nano')
ftp.retrlines('LIST')
print('retrieving file {}'.format(FN))
ftp.retrbinary('RETR %s'%FN, open('%s'%FN, 'wb').write)
ftp.quit()
