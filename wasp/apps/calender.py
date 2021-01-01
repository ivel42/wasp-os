# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2021 Andreas Lefevre

"""Calender
~~~~~~~~~~~

Shows special days.

For calculation the calender formulas of Christian Zeller will be used.
"""

#import wasp

WEEK_DAYS_DE = {0: 'Samstag',
                1: 'Sonntag',
                2: 'Montag',
                3: 'Dienstag',
                4: 'Mittwoch',
                5: 'Donnerstag',
                6: 'Freitag'}

DAYS_PER_MONTH = { 1: 31,
                   3: 31,
                   4: 30,
                   5: 31,
                   6: 30,
                   7: 31,
                   8: 30,
                   9: 31,
                  10: 31,
                  11: 30,
                  12: 31}



class Calender():
    """
    """

class Year:
    def __init__(self, yh, year):
        self.yh   = yh   # year hundred
        self.year = year # year - the last 2 digits
        self.update()

    def update(self):
        self.easter = getEaster(self.yh, self.year)
        self.ref1 = Day(27, 11, self.yh, self.year) # needed for 1. Advent
        self.ref2 = Day( 1,  5, self.yh, self.year) # needed for Muttertag
        self.ref3 = Day(23, 11, self.yh, self.year) # needed for Buß und Bettag
        self.ref4 = Day( 1, 10, self.yh, self.year) # needed for Erntedank
        self.ref5 = Day( 1,  4, self.yh, self.year) # needed for Sommerzeit
        self.ref6 = Day( 1, 11, self.yh, self.year) # needed for Normalzeit

class Day:
    """
    """
    def __init__(self, day, mon, yh, year):
        self.day  = day  # day of the month
        self.mon  = mon  # month of the year
        self.yh   = yh   # year hundred
        self.year = year # year - the last 2 digits

    def increment(self, daysToAdd):
        daysOfMonth = self.daysOfMonth
        for ii in range(daysToAdd):
            if(self.day < daysOfMonth):
                self.day += 1
            else:
                self.day = 1
                if (self.mon < 12):
                    self.mon += 1
                else:
                    self.mon = 1
                    if (self.year < 99):
                        self.year += 1
                    else:
                        self.year = 0
                        self.yh += 1                
                daysOfMonth = self.daysOfMonth

    def decrement(self, daysToSub):
        for ii in range(daysToSub):
            if(self.day > 1):
                self.day -= 1
            else:
                if (self.mon > 1):
                    self.mon -= 1
                else:
                    self.mon = 12
                    if (self.year > 1):
                        self.year -= 1
                    else:
                        self.year = 99
                        self.yh -= 1                
                self.day = self.daysOfMonth

    @property
    def wd(self):
        """
        weekDay in format So: 1, Mo: 2, Di: 3, Mi: 4, Do: 5, Fr: 6, Sa: 0
        """
        mon  = self.mon
        year = self.year

        # Month to convert after Zeller - jan, feb will be 13 & 14 month of the year before
        if ( (mon == 1) or (mon == 2) ):
            mon  = mon  + 12
            year = year - 1
        
        # Weekday calculation after Christian Zeller
        # Sa: 0, So: 1, Mo: 2, Di: 3, Mi: 4, Do: 5, Fr: 6

        aktWoTag = (self.day + int(((mon+1)*26)/10) + self.year + int(self.year/4) + int(self.yh/4) - 2*self.yh) % 7
        aktWoTag = aktWoTag + 7 if (aktWoTag < 0) else aktWoTag
        
        return aktWoTag

    @property
    def daysOfMonth(self):
        return getDaysPerMonth(self.mon, self.yh, self.year)

    def incToWeekDay(self, nextWeekDay):
        """
        Increments to the next day of the week.

        weekDay in format So: 1, Mo: 2, Di: 3, Mi: 4, Do: 5, Fr: 6, Sa: 0
        """

        currentWeekDay = self.wd

        if( nextWeekDay > currentWeekDay ):
            self.increment(nextWeekDay - currentWeekDay)
            #printf("aktW: %i, gesW: %i -> %i tage addiern\n",aktWoTag,sWoTag,sWoTag-aktWoTag);
        if( nextWeekDay < currentWeekDay ):
            self.increment(7 - currentWeekDay + nextWeekDay)
            #printf("aktW: %i, gesW: %i -> %i tage addiern\n",aktWoTag,sWoTag,7-aktWoTag+sWoTag);


    def isSpecialDay(self):
        pass

def getEaster(jh, year):

    # Berechnung nach Christian Zeller
    
    a = (5 * jh + year) % 19
    g = jh - int(jh / 4) - int(((8 * jh) + 13) / 25)
    b = ((19 * a) + 15 + g) % 30
    d = (b + year + int(year/4) + int(jh/4) + 2 - (2 * jh)) % 7
    d = d + 7 if ( d < 0 ) else d
    # Sonderfallbehandlung
    if( ((d == 0) and (b == 29)) or ((d == 0) and (b == 28) and (a > 10)) ):
        d = 7
    daysAfter21M = b + 7 - int(d)
    
     # Obige Formeln bestimmen wieviele Tage Ostersonntag nach dem 21.3 ist
    easter = Day(21, 3, jh, year)
    easter.increment(daysAfter21M)

    return easter

def getDaysPerMonth(mon, yh, year):

    if not (mon == 2):
        d = DAYS_PER_MONTH.get(mon)
    else:
        if((year % 4) == 0): # wenn das jahr durch 4 teilbar ist schaltjahr
            d = 29
            if(year == 0): # außer volles jh
                d = 28
                if((yh % 4) == 0): # ausnahme der ausnahme: jh durch 4 teilbar
                    d = 29
        else:
            d = 28
    return d

