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

def ckeckCW(day, cw):
    calCw = day.cw
    if calCw != cw:
        logging.error(f'CW is {calCw} but should be {cw} on {day}!')
    else:
        logging.info(f'CW is right for {day}!')


def ckeckDiff():
    t1 = Day(27, 11, 20, 20)
    t2 = Day(27, 11, 20, 21)
    
    diff1 = t2 - t1
    diff2 = t1 - t2

    print(diff1, diff2)

def checkMoCw1(calYear, day, mon, yh, year):
    """
    docstring
    """
    pass
    test = getMoCw1(calYear.yh, calYear.year)
    if(test.wd != 2):
        logging.error('not monday!')
    elif test.yh != yh or test.year != year:
        logging.error('wrong year!')
    elif test.day != day or test.mon != mon:
        logging.error('wrong day! - ' + str(test))
    else:
        logging.info('MoCw1 right for calender year ' + str(calYear))


def checkSpecialDay(year, day, mon, name ):

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

    year = Year(20,20)

    for key, value in year.specialDays.items():
        print(key + ' | ' + str(value))


    #test 2020
    year = Year(20,20) 
    checkMoCw1(year, 30, 12, 20, 19)
    checkSpecialDay(year,  1,  1, "New Year")
    checkSpecialDay(year,  6,  1, "Holy three kings")
    checkSpecialDay(year,  8,  3, "Women's Day")
    checkSpecialDay(year, 10,  4, "Good Friday")
    checkSpecialDay(year, 12,  4, "Easter Sunday")
    checkSpecialDay(year, 13,  4, "Easter Monday")
    checkSpecialDay(year,  1,  5, "Labor Day (de)")
    checkSpecialDay(year,  8,  5, "Victory in Europe")
    checkSpecialDay(year, 21,  5, "Fathers day")
    checkSpecialDay(year, 31,  5, "Pentecost Sunday")
    checkSpecialDay(year,  1,  6, "Whit Monday")
    checkSpecialDay(year, 11,  6, "Corpus Christi")
    checkSpecialDay(year,  8,  8, "Peace Festival Augsburg")
    checkSpecialDay(year, 15,  8, "Assumption Day")
    checkSpecialDay(year, 20,  9, "Children's Day")
    checkSpecialDay(year,  3, 10, "Day of German unity")
    checkSpecialDay(year, 31, 10, "Reformation Day 1517")
    checkSpecialDay(year,  1, 11, "All Saints Day")
    checkSpecialDay(year, 18, 11, "Buß- und Bettag")
    checkSpecialDay(year, 25, 12, "First christmasday")
    checkSpecialDay(year, 26, 12, "Second christmasday")
    checkSpecialDay(year, 29,  3, "Summertime (eu)")
    checkSpecialDay(year, 25, 10, "Normaltime (eu)")
    
    ##test 2021
    year = Year(20,21) 
    checkMoCw1(year, 4, 1, 20, 21)
    checkSpecialDay(year,  1,  1, "New Year")
    checkSpecialDay(year,  6,  1, "Holy three kings")
    checkSpecialDay(year,  8,  3, "Women's Day")
    checkSpecialDay(year,  2,  4, "Good Friday")
    checkSpecialDay(year,  4,  4, "Easter Sunday")
    checkSpecialDay(year,  5,  4, "Easter Monday")
    checkSpecialDay(year,  1,  5, "Labor Day (de)")
    checkSpecialDay(year,  8,  5, "Victory in Europe")
    checkSpecialDay(year, 13,  5, "Fathers day")
    checkSpecialDay(year, 23,  5, "Pentecost Sunday")
    checkSpecialDay(year, 24,  5, "Whit Monday")
    checkSpecialDay(year,  3,  6, "Corpus Christi")
    checkSpecialDay(year,  8,  8, "Peace Festival Augsburg")
    checkSpecialDay(year, 15,  8, "Assumption Day")
    checkSpecialDay(year, 20,  9, "Children's Day")
    checkSpecialDay(year,  3, 10, "Day of German unity")
    checkSpecialDay(year, 31, 10, "Reformation Day 1517")
    checkSpecialDay(year,  1, 11, "All Saints Day")
    checkSpecialDay(year, 17, 11, "Buß- und Bettag")
    checkSpecialDay(year, 25, 12, "First christmasday")
    checkSpecialDay(year, 26, 12, "Second christmasday")
    checkSpecialDay(year, 28,  3, "Summertime (eu)")
    checkSpecialDay(year, 31, 10, "Normaltime (eu)")

    ##test 2022
    year = Year(20,22) 
    checkMoCw1(year, 3, 1, 20, 22)
    checkSpecialDay(year,  1,  1, "New Year")
    checkSpecialDay(year,  6,  1, "Holy three kings")
    checkSpecialDay(year,  8,  3, "Women's Day")
    checkSpecialDay(year, 15,  4, "Good Friday")
    checkSpecialDay(year, 17,  4, "Easter Sunday")
    checkSpecialDay(year, 18,  4, "Easter Monday")
    checkSpecialDay(year,  1,  5, "Labor Day (de)")
    checkSpecialDay(year,  8,  5, "Victory in Europe")
    checkSpecialDay(year, 26,  5, "Fathers day")
    checkSpecialDay(year,  5,  6, "Pentecost Sunday")
    checkSpecialDay(year,  6,  6, "Whit Monday")
    checkSpecialDay(year, 16,  6, "Corpus Christi")
    checkSpecialDay(year,  8,  8, "Peace Festival Augsburg")
    checkSpecialDay(year, 15,  8, "Assumption Day")
    checkSpecialDay(year, 20,  9, "Children's Day")
    checkSpecialDay(year,  3, 10, "Day of German unity")
    checkSpecialDay(year, 31, 10, "Reformation Day 1517")
    checkSpecialDay(year,  1, 11, "All Saints Day")
    checkSpecialDay(year, 16, 11, "Buß- und Bettag")
    checkSpecialDay(year, 25, 12, "First christmasday")
    checkSpecialDay(year, 26, 12, "Second christmasday")
    checkSpecialDay(year, 27,  3, "Summertime (eu)")
    checkSpecialDay(year, 30, 10, "Normaltime (eu)")

    ##test 2023
    year = Year(20,23) 
    checkMoCw1(year, 2, 1, 20, 23)
    checkSpecialDay(year,  1,  1, "New Year")
    checkSpecialDay(year,  6,  1, "Holy three kings")
    checkSpecialDay(year,  8,  3, "Women's Day")
    checkSpecialDay(year,  7,  4, "Good Friday")
    checkSpecialDay(year,  9,  4, "Easter Sunday")
    checkSpecialDay(year, 10,  4, "Easter Monday")
    checkSpecialDay(year,  1,  5, "Labor Day (de)")
    checkSpecialDay(year,  8,  5, "Victory in Europe")
    checkSpecialDay(year, 18,  5, "Fathers day")
    checkSpecialDay(year, 28,  5, "Pentecost Sunday")
    checkSpecialDay(year, 29,  5, "Whit Monday")
    checkSpecialDay(year,  8,  6, "Corpus Christi")
    checkSpecialDay(year,  8,  8, "Peace Festival Augsburg")
    checkSpecialDay(year, 15,  8, "Assumption Day")
    checkSpecialDay(year, 20,  9, "Children's Day")
    checkSpecialDay(year,  3, 10, "Day of German unity")
    checkSpecialDay(year, 31, 10, "Reformation Day 1517")
    checkSpecialDay(year,  1, 11, "All Saints Day")
    checkSpecialDay(year, 22, 11, "Buß- und Bettag")
    checkSpecialDay(year, 25, 12, "First christmasday")
    checkSpecialDay(year, 26, 12, "Second christmasday")
    checkSpecialDay(year, 26,  3, "Summertime (eu)")
    checkSpecialDay(year, 29, 10, "Normaltime (eu)")

    ckeckCW(Day( 1,  1, 20, 20),  1)
    ckeckCW(Day( 5,  1, 20, 20),  1)
    ckeckCW(Day( 6,  1, 20, 20),  2)
    ckeckCW(Day( 2,  3, 20, 20), 10)
    ckeckCW(Day(12,  4, 20, 20), 15)
    ckeckCW(Day(16,  9, 20, 20), 38)
    ckeckCW(Day(31, 12, 20, 20), 53)

    ckeckCW(Day( 1,  1, 20, 21), 53)
    ckeckCW(Day( 4,  1, 20, 21),  1)
    ckeckCW(Day(17,  1, 20, 21),  2)
    ckeckCW(Day(31,  3, 20, 21), 13)
    ckeckCW(Day(31, 12, 20, 21), 52)

if __name__ == '__main__':
    main()
