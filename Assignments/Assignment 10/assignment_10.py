import argparse
import logging 

logger = logging.getLogger()
logging.basicConfig(level = logging.DEBUG, format = f'%(asctime)s %(levelname)s : %(message)s')
logging.info("This is an info log message")
logging.warning("This is an warning log message")
logging.debug("This is an debug log message")
logging.error("This is an error log message")
logging.critical("This is an critical log message")
print(" ")

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--summation", help = "This will determine the sum from 0 to n", action = "store_true")
parser.add_argument("number", help= "This number will printed from one to the number")  
args = parser.parse_args()

def sigma_notation_formula(number):
    logging.info("You have entered the number: " + str(number))
    temp = 0
    for index in range(number + 1):
        temp += index
    return temp

sigma_sum = sigma_notation_formula(int(args.number))
logging.info("The sum is " + str(sigma_sum))



