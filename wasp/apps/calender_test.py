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

def checkDay(year, day, mon, name ):

    tmp = year.isSpecialDay(day,mon)
    if len(tmp) == 0:
        logging.error('date not found for ' + name)
    else:
        notMatchingNames = list()
        for item in tmp:
            if name == item._name:
                logging.info('date found for ' + name)
                break
            else:
                notMatchingNames.append(item._name)
        else:
            log = 'date found for ' + name + ' but with the names '
            for n in notMatchingNames:
                log += n + ', '

            logging.error(log[0:-2])
        pass

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

    easter = getEaster(20,21)
    logging.info(f'Easter is on {WEEK_DAYS_DE.get(easter.wd)} - {easter.day}.{easter.mon}.{easter.yh}{easter.year}')

    easter = getEaster(20,20)
    logging.info(f'Easter is on {WEEK_DAYS_DE.get(easter.wd)} - {easter.day}.{easter.mon}.{easter.yh}{easter.year}')

    year = Year(20,21)

    for key, value in year.specialDays.items():
        print(key + ' | ' + str(value))


    #test 2020
    year = Year(20,20) 
    checkDay(year,  1,  1, "New Year")
    checkDay(year,  6,  1, "Holy three kings")
    checkDay(year,  8,  3, "Women's Day")
    checkDay(year, 10,  4, "Good Friday")
    checkDay(year, 12,  4, "Easter Sunday")
    checkDay(year, 13,  4, "Easter Monday")
    checkDay(year,  1,  5, "Labor Day (de)")
    checkDay(year,  8,  5, "Victory in Europe")
    checkDay(year, 21,  5, "Fathers day")
    checkDay(year, 31,  5, "Pentecost Sunday")
    checkDay(year,  1,  6, "Whit Monday")
    checkDay(year, 11,  6, "Corpus Christi")
    checkDay(year,  8,  8, "Peace Festival Augsburg")
    checkDay(year, 15,  8, "Assumption Day")
    checkDay(year, 20,  9, "Children's Day")
    checkDay(year,  3, 10, "Day of German unity")
    checkDay(year, 31, 10, "Reformation Day 1517")
    checkDay(year,  1, 11, "All Saints Day")
    checkDay(year, 18, 11, "Buß- und Bettag")
    checkDay(year, 25, 12, "First christmasday")
    checkDay(year, 26, 12, "Second christmasday")
    checkDay(year, 29,  3, "Summertime (eu)")
    checkDay(year, 25, 10, "Normaltime (eu)")

    #test 2021
    year = Year(20,21) 
    checkDay(year,  1,  1, "New Year")
    checkDay(year,  6,  1, "Holy three kings")
    checkDay(year,  8,  3, "Women's Day")
    checkDay(year,  2,  4, "Good Friday")
    checkDay(year,  4,  4, "Easter Sunday")
    checkDay(year,  5,  4, "Easter Monday")
    checkDay(year,  1,  5, "Labor Day (de)")
    checkDay(year,  8,  5, "Victory in Europe")
    checkDay(year, 13,  5, "Fathers day")
    checkDay(year, 23,  5, "Pentecost Sunday")
    checkDay(year, 24,  5, "Whit Monday")
    checkDay(year,  3,  6, "Corpus Christi")
    checkDay(year,  8,  8, "Peace Festival Augsburg")
    checkDay(year, 15,  8, "Assumption Day")
    checkDay(year, 20,  9, "Children's Day")
    checkDay(year,  3, 10, "Day of German unity")
    checkDay(year, 31, 10, "Reformation Day 1517")
    checkDay(year,  1, 11, "All Saints Day")
    checkDay(year, 17, 11, "Buß- und Bettag")
    checkDay(year, 25, 12, "First christmasday")
    checkDay(year, 26, 12, "Second christmasday")
    checkDay(year, 28,  3, "Summertime (eu)")
    checkDay(year, 31, 10, "Normaltime (eu)")

    #test 2021
    year = Year(20,21) 
    checkDay(year,  1,  1, "New Year")
    checkDay(year,  6,  1, "Holy three kings")
    checkDay(year,  8,  3, "Women's Day")
    checkDay(year,  2,  4, "Good Friday")
    checkDay(year,  4,  4, "Easter Sunday")
    checkDay(year,  5,  4, "Easter Monday")
    checkDay(year,  1,  5, "Labor Day (de)")
    checkDay(year,  8,  5, "Victory in Europe")
    checkDay(year, 13,  5, "Fathers day")
    checkDay(year, 23,  5, "Pentecost Sunday")
    checkDay(year, 24,  5, "Whit Monday")
    checkDay(year,  3,  6, "Corpus Christi")
    checkDay(year,  8,  8, "Peace Festival Augsburg")
    checkDay(year, 15,  8, "Assumption Day")
    checkDay(year, 20,  9, "Children's Day")
    checkDay(year,  3, 10, "Day of German unity")
    checkDay(year, 31, 10, "Reformation Day 1517")
    checkDay(year,  1, 11, "All Saints Day")
    checkDay(year, 17, 11, "Buß- und Bettag")
    checkDay(year, 25, 12, "First christmasday")
    checkDay(year, 26, 12, "Second christmasday")
    checkDay(year, 28,  3, "Summertime (eu)")
    checkDay(year, 31, 10, "Normaltime (eu)")

    #test 2022
    year = Year(20,22) 
    checkDay(year,  1,  1, "New Year")
    checkDay(year,  6,  1, "Holy three kings")
    checkDay(year,  8,  3, "Women's Day")
    checkDay(year, 15,  4, "Good Friday")
    checkDay(year, 17,  4, "Easter Sunday")
    checkDay(year, 18,  4, "Easter Monday")
    checkDay(year,  1,  5, "Labor Day (de)")
    checkDay(year,  8,  5, "Victory in Europe")
    checkDay(year, 26,  5, "Fathers day")
    checkDay(year,  5,  6, "Pentecost Sunday")
    checkDay(year,  6,  6, "Whit Monday")
    checkDay(year, 16,  6, "Corpus Christi")
    checkDay(year,  8,  8, "Peace Festival Augsburg")
    checkDay(year, 15,  8, "Assumption Day")
    checkDay(year, 20,  9, "Children's Day")
    checkDay(year,  3, 10, "Day of German unity")
    checkDay(year, 31, 10, "Reformation Day 1517")
    checkDay(year,  1, 11, "All Saints Day")
    checkDay(year, 16, 11, "Buß- und Bettag")
    checkDay(year, 25, 12, "First christmasday")
    checkDay(year, 26, 12, "Second christmasday")
    checkDay(year, 27,  3, "Summertime (eu)")
    checkDay(year, 30, 10, "Normaltime (eu)")

    #test 2023
    year = Year(20,23) 
    checkDay(year,  1,  1, "New Year")
    checkDay(year,  6,  1, "Holy three kings")
    checkDay(year,  8,  3, "Women's Day")
    checkDay(year,  7,  4, "Good Friday")
    checkDay(year,  9,  4, "Easter Sunday")
    checkDay(year, 10,  4, "Easter Monday")
    checkDay(year,  1,  5, "Labor Day (de)")
    checkDay(year,  8,  5, "Victory in Europe")
    checkDay(year, 18,  5, "Fathers day")
    checkDay(year, 28,  5, "Pentecost Sunday")
    checkDay(year, 29,  5, "Whit Monday")
    checkDay(year,  8,  6, "Corpus Christi")
    checkDay(year,  8,  8, "Peace Festival Augsburg")
    checkDay(year, 15,  8, "Assumption Day")
    checkDay(year, 20,  9, "Children's Day")
    checkDay(year,  3, 10, "Day of German unity")
    checkDay(year, 31, 10, "Reformation Day 1517")
    checkDay(year,  1, 11, "All Saints Day")
    checkDay(year, 22, 11, "Buß- und Bettag")
    checkDay(year, 25, 12, "First christmasday")
    checkDay(year, 26, 12, "Second christmasday")
    checkDay(year, 26,  3, "Summertime (eu)")
    checkDay(year, 29, 10, "Normaltime (eu)")


if __name__ == '__main__':
    main()
