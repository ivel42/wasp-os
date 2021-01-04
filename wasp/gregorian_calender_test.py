# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2021 Andreas Lefevre

"""
"""

import logging
import optparse
from gregorian_calender import *
import gregorian_calender_cfg_de as cfg


# import pdb # debugging e.g. pdb.set_trace() for breakpoint
LOGGING_LEVELS = {'critical': logging.CRITICAL,
                  'error'   : logging.ERROR,
                  'warning' : logging.WARNING,
                  'info'    : logging.INFO,
                  'debug'   : logging.DEBUG}

class Colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def ckeckCW(day, cw):
    calCw = day.cw
    if calCw != cw:
        logging.error(f'CW is {calCw} but should be {cw} on {day}!')
    else:
        logging.info(f'CW is right for {day}!')

def printCal( mon, year):
    y = Year(year) 
    calStr = ''
    calStr += f'{cfg.MONTH_NAMES[mon]} {year}\n'
    calStr += 'KW Mo Di Mi Do Fr Sa So\n'
    d = Day(1, mon, year)
    while d.mon == mon:
        if d.cw < 10:
            calStr += ' '
        calStr += f'{d.cw}'
        offset = 3 * d.wd_norm
        for ii in range(offset):
            calStr += ' '
        while d.mon == mon:
            color = False
            if d.day < 10:
                calStr += '  '
            else:
                calStr += ' '
            dType = y.specialDayType(d.day, d.mon)
            if d.wd_norm == 6: # So
                calStr += Colour.RED
                color = True
            if dType == SpecialDayType.INFO_DAY: 
                calStr += Colour.CYAN
                color = True
            if dType == SpecialDayType.HOLIDAY: 
                calStr += Colour.GREEN
                color = True
            calStr += f'{d.day}'
            if color: 
                calStr += Colour.END
            d.increment(1)
            if d.wd_norm == 0:
                if d.mon == mon:
                    calStr += '\n'
                break
    print(calStr+'\n')

def ckeckDiff():
    t1 = Day(27, 11, 2020)
    t2 = Day(27, 11, 2021)
    
    diff1 = t2 - t1
    diff2 = t1 - t2

    print(diff1, diff2)

def checkMoCw1(calYear, day, mon, year):
    """
    docstring
    """
    pass
    test = getMoCw1(calYear.year)
    if(test.__wd__ != 2):
        logging.error('not monday!')
    elif test.year != year:
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

    easter = getEaster(20, 21)
    logging.info(f'Easter is on {cfg.WEEK_DAYS.get(easter.__wd__)} - {easter.day}.{easter.mon}.{easter.yh}{easter.year}')

    easter = getEaster(20, 20)
    logging.info(f'Easter is on {cfg.WEEK_DAYS.get(easter.__wd__)} - {easter.day}.{easter.mon}.{easter.yh}{easter.year}')

    year = Year(2020)

    for key, value in year.specialDays.items():
        print(key + ' | ' + str(value))


    # test 2020
    year = Year(2020) 
    checkMoCw1(year, 30, 12, 2019)
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
    
    # test 2021
    year = Year(2021) 
    checkMoCw1(year, 4, 1, 2021)
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

    # test 2022
    year = Year(2022) 
    checkMoCw1(year, 3, 1, 2022)
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

    # test 2023
    year = Year(2023) 
    checkMoCw1(year, 2, 1, 2023)
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

    # test 1848
    year = Year(1848) 
    checkMoCw1(year, 3, 1, 1848)
    checkSpecialDay(year,  1,  1, "New Year")
    checkSpecialDay(year,  6,  1, "Holy three kings")
    checkSpecialDay(year, 14,  2, "Valentine's day")
    checkSpecialDay(year,  7,  3, "Shrove Tuesday")
    checkSpecialDay(year,  8,  3, "Ash Wednesday")
    checkSpecialDay(year, 21,  4, "Good Friday")
    checkSpecialDay(year, 23,  4, "Easter Sunday")
    checkSpecialDay(year, 24,  4, "Easter Monday")
    checkSpecialDay(year,  1,  6, "Ascension of Christ")
    checkSpecialDay(year, 11,  6, "Pentecost Sunday")
    checkSpecialDay(year, 12,  6, "Whit Monday")
    checkSpecialDay(year, 22,  6, "Corpus Christi")
    checkSpecialDay(year,  1, 11, "All Saints Day")
    checkSpecialDay(year, 11, 11, "Martin's Day")
    checkSpecialDay(year,  3, 12, "1 Advent")
    checkSpecialDay(year,  6, 12, "St. Nicholas Day")
    checkSpecialDay(year, 24, 12, "Christmas eve")
    checkSpecialDay(year, 25, 12, "First christmasday")
    checkSpecialDay(year, 31, 12, "New Year's Eve")
  
    # test 1583 - first valid year - gregorian calender!
    year = Year(1583) 
    checkMoCw1(year, 3, 1, 1583)
    checkSpecialDay(year,  1,  1, "New Year")
    checkSpecialDay(year,  6,  1, "Holy three kings")
    checkSpecialDay(year, 14,  2, "Valentine's day")
    checkSpecialDay(year, 22,  2, "Shrove Tuesday")
    checkSpecialDay(year, 23,  2, "Ash Wednesday")
    checkSpecialDay(year,  8,  4, "Good Friday")
    checkSpecialDay(year, 10,  4, "Easter Sunday")
    checkSpecialDay(year, 11,  4, "Easter Monday")
    checkSpecialDay(year, 19,  5, "Ascension of Christ")
    checkSpecialDay(year, 29,  5, "Pentecost Sunday")
    checkSpecialDay(year, 30,  5, "Whit Monday")
    checkSpecialDay(year,  9,  6, "Corpus Christi")
    checkSpecialDay(year,  1, 11, "All Saints Day")
    checkSpecialDay(year, 11, 11, "Martin's Day")
    checkSpecialDay(year, 27, 11, "1 Advent")
    checkSpecialDay(year,  6, 12, "St. Nicholas Day")
    checkSpecialDay(year, 24, 12, "Christmas eve")
    checkSpecialDay(year, 25, 12, "First christmasday")
    checkSpecialDay(year, 31, 12, "New Year's Eve")
  
    ckeckCW(Day( 1,  1, 2020),  1)
    ckeckCW(Day( 5,  1, 2020),  1)
    ckeckCW(Day( 6,  1, 2020),  2)
    ckeckCW(Day( 2,  3, 2020), 10)
    ckeckCW(Day(12,  4, 2020), 15)
    ckeckCW(Day(16,  9, 2020), 38)
    ckeckCW(Day(31, 12, 2020), 53)

    ckeckCW(Day( 1,  1, 2021), 53)
    ckeckCW(Day( 4,  1, 2021),  1)
    ckeckCW(Day(17,  1, 2021),  2)
    ckeckCW(Day(31,  3, 2021), 13)
    ckeckCW(Day(31, 12, 2021), 52)

    ckeckCW(Day( 1,  1, 1847), 53)
    ckeckCW(Day( 1,  1, 1848), 52)
    ckeckCW(Day( 1,  1, 1849),  1)

    printCal( 1, 2021)
    printCal( 2, 2021)
    printCal( 3, 2021)
    printCal( 4, 2021)
    printCal( 5, 2021)
    printCal( 6, 2021)
    printCal( 7, 2021)
    printCal( 8, 2021)
    printCal( 9, 2021)
    printCal( 10, 2021)
    printCal( 11, 2021)
    printCal( 12, 2021)

if __name__ == '__main__':
    main()
