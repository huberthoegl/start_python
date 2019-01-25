# from: Hetland, Beginning Python, Apress

import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
       datefmt="%a, %d %b %Y %H:%M:%S", 
       level=logging.INFO, 
       filename='mylog.log')

logging.info('Starting program')

logging.info('Trying to divide 1 by 0')

# print(1/0)

logging.info('The division succeeded')

logging.info('Ending program')
