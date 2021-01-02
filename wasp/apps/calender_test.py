# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2021 Andreas Lefevre

"""
"""

import logging
import optparse
from calender import *

# import pdb # debugging e.g. pdb.set_trace() for breakpoint
LOGGING_LEVELS = {'critical': logging.CRITICAL,
                  'error'   : logging.ERROR,
                  'warning' : logging.WARNING,
                  'info'    : logging.INFO,
                  'debug'   : logging.DEBUG}

def main():
    """
    """
    # : parser object to get command line attributes
    parser = optparse.OptionParser()
    parser.add_option('-l', '--logging-level', help = 'Logging level: eg. critical, error, warning, info, debug')
    parser.add_option('-f', '--logging-file', help = 'Logging file name')
    (options, args) = parser.parse_args()

    if options.logging_level is None:
        logging_level = logging.DEBUG
    else:
        logging_level = LOGGING_LEVELS.get(options.logging_level, logging.NOTSET)

    logging.basicConfig(level = logging_level, filename = options.logging_file,
                        format = '%(asctime)s %(levelname)s: %(message)s',
                        datefmt = '%Y-%m-%d %H:%M:%S')
    logging.info('Logging Lever set to ' + str(logging_level))

    easter = getEaster(20,20)
    logging.info(f'Easter is on {WEEK_DAYS_DE.get(easter.wd)} - {easter.day}.{easter.mon}.{easter.yh}{easter.year}')

    easter = getEaster(20,21)
    logging.info(f'Easter is on {WEEK_DAYS_DE.get(easter.wd)} - {easter.day}.{easter.mon}.{easter.yh}{easter.year}')

    year = Year(20,21)

    for key, value in year.specialDays.items():
        print(key + ' | ' + str(value))


    print(year.isSpecialDay(2,1))

if __name__ == '__main__':
    main()
