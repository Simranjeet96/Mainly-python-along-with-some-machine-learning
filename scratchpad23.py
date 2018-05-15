import logging
import employee
logger=logging.getLogger(__name__)
logging.basicConfig(filename='logging.log',level=logging.INFO,format='%(asctime)s:%(name)s:%(message)s')

def add(x,y):
    return x+y

def divide(x,y):
   return x/y

logging.info(add(1,2))
logging.info(divide(3,4))    
logging.info(divide(0,1))
