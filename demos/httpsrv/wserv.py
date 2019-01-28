
'''
taken from Python 3.6 standard lib: 21.22. http.server 
must run with Python >= 3.6

python wserv.py

Run it at DLR Schul10 (129.247.170.10, AIRP-010)
Other PCs can see the current directory with the URL
http://129.247.170.10:20000.

H. Hoegl, 20.2.2018
'''

import http.server
import socketserver

PORT = 20000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

