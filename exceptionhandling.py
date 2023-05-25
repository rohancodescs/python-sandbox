#Errors and exception handling & logging
import logging
class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooLowError('Value is too low', x)

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)


print("\n---------------------\n")

# import logging

logging.basicConfig(filename='mylog.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

#creating a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)