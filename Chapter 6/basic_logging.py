"""
Using the logging module

import logging

logging.debug('debug-level message') Diagnostic information useful for debugging
logging.info('info-level message') General information about program execution results
logging.warning('warning-level message') Something unexpected, or approaching a problem
logging.error('error-level message') Unable to perform a specific operation due to problem
logging.critical('critical-level message') Program may not be able to continue, serious error

Default logging is only warning and above, but can be configured by:
logging.basicConfig(level=logging.DEBUG)

basicConfig can only ever be invoked once before the logging starts. Ivoking this after the first log message will not
do anything!
"""

# Demonstrate the logging API in Python

import logging


def main():
    # Use basicConfig to configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        filename='output.log',
        filemode='w'
    )

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

    # Output formatted string to the log
    logging.info('Here\'s a {} variable and an int'.format('string', 10))


if __name__ == '__main__':
    main()
