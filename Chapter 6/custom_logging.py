"""
Customized logging

Logging module is flexible; can customize based on needs

basicConfig takes in some arguments that control the precise formatting of the messages:

basicConfig(
    format=formatstr,
    datefmt=date_format_str
)

Some tokens used:
%(asctime)s
%(filename)s
%(funcName)s
%(levelname)s
%(levelno)d
%(lineno)d
%(message)s
%(module)s
"""

# Demonstrate the logging API in Python

import logging

extra_data = {
    'user': 'joe@example.com'
}


def my_function():
    logging.debug('This is a debug level message', extra=extra_data)


def main():
    # Set the output file and debug level
    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     filename='custom_output.log',
    #     filemode='w'
    # )

    # let's add the custom formatting specifications
    format_string = 'User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d %(message)s'
    date_string = '%m/%d/%Y %I:%M:%S %p'
    logging.basicConfig(
        level=logging.DEBUG,
        filename='custom_output.log',
        filemode='w',
        format=format_string,
        datefmt=date_string
    )

    logging.debug('This is a debug message', extra=extra_data)
    logging.info('This is an info message', extra=extra_data)
    logging.warning('This is a warning message', extra=extra_data)
    logging.error('This is an error message', extra=extra_data)
    logging.critical('This is a critical message', extra=extra_data)
    my_function()


if __name__ == '__main__':
    main()
