# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2021 Andreas Lefevre

"""Calender
~~~~~~~~~~~

Shows special days.

For calculation the calender formulas of Christian Zeller will be used.
"""

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

class SpecialDayType():
    IGNORE   = 0
    INFO_DAY = 1
    HOLIDAY  = 2

colors = {'white'  : 0xffff,
          'red'    : 0xf800,
          'yellow' : 0xffe0,
          'green'  : 0x07e0, 
          'cyan'   : 0x07ff,
          'blue'   : 0xffff,
          'magenta': 0xf81f}

dayColors = {'sunday'  : colors['red'],
             'holiday' : colors['magenta'],
             'infoday' : colors['cyan']}

import copy
import gregorian_calender_cfg_uk as cfg

class Year:
    def __init__(self, year):
        self.year = year
        self.specialDays = dict()
        self.update()

    def __str__(self):
        return f'{self.year}'

    def addSpecialDay(self, specialDay):
        self.specialDays[specialDay._name] = specialDay

    def update(self):
        yh   = self.year // 100 # year hundred
        ys   = self.year %  100 # year - the last 2 digits

        self.easter = getEaster(yh, ys)
        self.moCw1  = getMoCw1( self.year)
        self.ref1 = Day(27, 11, self.year) # needed for 1. Advent
        self.ref2 = Day( 1,  5, self.year) # needed for Muttertag
        self.ref3 = Day(23, 11, self.year) # needed for Buß und Bettag
        self.ref4 = Day( 1, 10, self.year) # needed for Erntedank
        self.ref5 = Day( 1,  4, self.year) # needed for Sommerzeit
        self.ref6 = Day( 1, 11, self.year) # needed for Normalzeit


        self.addSpecialDay(SpecialDay(name="Women's Shrovetide",   day=self.easter, offset= -52))
        self.addSpecialDay(SpecialDay(name="Carnival Monday",      day=self.easter, offset= -48)) 
        self.addSpecialDay(SpecialDay(name="Shrove Tuesday",       day=self.easter, offset= -47)) 
        self.addSpecialDay(SpecialDay(name="Ash Wednesday",        day=self.easter, offset= -46)) 
        self.addSpecialDay(SpecialDay(name="Palm Sunday",          day=self.easter, offset=  -7))
        self.addSpecialDay(SpecialDay(name="Maundy Thursday",      day=self.easter, offset=  -3)) 
        self.addSpecialDay(SpecialDay(name="Good Friday",          day=self.easter, offset=  -2)) 
        self.addSpecialDay(SpecialDay(name="Holy Saturday",        day=self.easter, offset=  -1)) 
        self.addSpecialDay(SpecialDay(name="Easter Sunday",        day=self.easter))              
        self.addSpecialDay(SpecialDay(name="Easter Monday",        day=self.easter, offset=   1)) 
        self.addSpecialDay(SpecialDay(name="White Sunday",         day=self.easter, offset=   7)) 
        self.addSpecialDay(SpecialDay(name="Fathers day",          day=self.easter, offset=  39)) 
        self.addSpecialDay(SpecialDay(name="Ascension of Christ",  day=self.easter, offset=  39)) 
        self.addSpecialDay(SpecialDay(name="Pentecost Sunday",     day=self.easter, offset=  49)) 
        self.addSpecialDay(SpecialDay(name="Whit Monday",          day=self.easter, offset=  50)) 
        self.addSpecialDay(SpecialDay(name="Corpus Christi",       day=self.easter, offset=  60)) 

        self.addSpecialDay(SpecialDay(name="Memorial Day (de)", day=self.ref1, offset=-14, incToWeekDay=1))
        self.addSpecialDay(SpecialDay(name="1 Advent",          day=self.ref1, incToWeekDay=1))            
        self.addSpecialDay(SpecialDay(name="2 Advent",          day=self.ref1, offset=7, incToWeekDay=1))  
        self.addSpecialDay(SpecialDay(name="3 Advent",          day=self.ref1, offset=14, incToWeekDay=1)) 
        self.addSpecialDay(SpecialDay(name="4 Advent",          day=self.ref1, offset=21, incToWeekDay=1)) 

        self.addSpecialDay(SpecialDay(name="Mother's Day",      day=self.ref2, offset=7, incToWeekDay=1)) 
        
        self.addSpecialDay(SpecialDay(name="Thanksgiving (de)", day=self.ref4, incToWeekDay=1)) 

        self.addSpecialDay(SpecialDay(name="Buß- und Bettag",   day=self.ref3, offset=-7, incToWeekDay=4)) 
        
        self.addSpecialDay(SpecialDay(name="Summertime (eu)",   day=self.ref5, offset= -7, incToWeekDay=1))
        self.addSpecialDay(SpecialDay(name="Normaltime (eu)",   day=self.ref6, offset= -7, incToWeekDay=1)) 

        
        self.addSpecialDay(SpecialDay(name="New Year",                      day= 1, mon= 1, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Holy three kings",              day= 6, mon= 1, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Valentine's day",               day=14, mon= 2, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Women's Day",                   day= 8, mon= 3, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Day of the beer",               day=23, mon= 4, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Labor Day (de)",                day= 1, mon= 5, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Europe day",                    day= 5, mon= 5, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Victory in Europe",             day= 8, mon= 5, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Constitution (de)",             day=23, mon= 5, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Popular uprising DDR 1953",     day=17, mon= 6, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Attack 1944",                   day=20, mon= 7, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Summer solstice",               day=21, mon= 7, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Peace Festival Augsburg",       day= 8, mon= 8, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Assumption Day",                day=15, mon= 8, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Children's Day",                day=20, mon= 9, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Begin WW2 1939",                day= 1, mon=10, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Day of German unity",           day= 3, mon=10, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Hiroshima 1945",                day= 6, mon=10, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Construction of the wall 1961", day=13, mon=10, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Reformation Day 1517",          day=31, mon=10, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="All Saints Day",                day= 1, mon=11, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="All Souls Day",                 day= 2, mon=11, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="October Revolution 1917",       day= 7, mon=11, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="9. November (Germany)",         day= 9, mon=11, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="St. Nicholas Day",              day= 6, mon=12, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Mary Conception",               day= 8, mon=12, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Martin's Day" ,                 day=11, mon=11, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Winter solstice",               day=22, mon=12, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Christmas eve" ,                day=24, mon=12, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="First christmasday",            day=25, mon=12, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Second christmasday",           day=26, mon=12, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="New Year's Eve",                day=31, mon=12, year=self.year)) 

        # days to add
        # UK https://de.wikipedia.org/wiki/Boxing_Day
        # US Birthday of Martin Luther King, Jr. - January 15–21 (Floating Monday)
        # US Washington's Birthday - February 15–21 (Floating Monday)
        # US Memorial Day - May 25–31 (Floating Monday)
        # US Independence Day - July 4 (Fixed)
        # US Labor Day - September 1–7 (Floating Monday)
        # US Columbus Day - October 8–14 (Floating Monday)
        # US Veterans Day - November 11 (Fixed)
        # US Thanksgiving Day - November 22–28 (Floating Thursday)
        # UK 2nd January (substitute day) (Scotland) https://www.timeanddate.com/holidays/uk/2nd-january
        # UK 1 Mar	St. David's Day (Wales) https://www.timeanddate.com/holidays/uk/st-david-day
        # UK 17 Mar	St Patrick's Day (Northern Ireland) https://www.timeanddate.com/holidays/uk/st-patricks-day
        # UK 23 Apr	St. George's Day https://www.timeanddate.com/holidays/uk/st-george-day
        # UK 3 May	Early May Bank Holiday https://www.timeanddate.com/holidays/uk/early-may-bank-holiday
        # UK 31 May	Spring Bank Holiday https://www.timeanddate.com/holidays/uk/spring-bank-holiday
        # UK 12 Jun	Queen's Birthday
        # UK 12 Jul	Battle of the Boyne (Northern Ireland) https://www.timeanddate.com/holidays/uk/orangemen-day
        # UK 2 Aug	Summer Bank Holiday (Scotland) https://www.timeanddate.com/holidays/uk/summer-bank-holiday
        # UK 30 Aug	Summer Bank Holiday (ENG, NIR, WAL) https://www.timeanddate.com/holidays/uk/summer-bank-holiday
        # 31 Oct	Halloween https://www.timeanddate.com/holidays/uk/halloween
        # UK 5 Nov	Guy Fawkes Day https://www.timeanddate.com/holidays/uk/guy-fawkes-day
        # UK 14 Nov	Remembrance Sunday https://www.timeanddate.com/holidays/uk/remembrance-sunday
        # UK 30 Nov	St Andrew's Day (Scotland) https://www.timeanddate.com/holidays/uk/st-andrew-day
        # UK 26 Dec	Boxing Day https://www.timeanddate.com/holidays/uk/boxing-day
        # UK 27 Dec	Bank Holiday https://www.timeanddate.com/holidays/uk/bank-holiday-dec-27
        # UK 28 Dec	Bank Holiday https://www.timeanddate.com/holidays/uk/bank-holiday-dec-28

    def isSpecialDay(self, day, mon):
        retval = list()
        for key, sDay in self.specialDays.items():
            if sDay.day == day and sDay.mon == mon:
                retval.append(sDay)

        return retval

    def specialDayType(self, day, mon):
        retval = 0
        for key, sDay in self.specialDays.items():
            if sDay.day == day and sDay.mon == mon:
                retval = max(retval, sDay.type)

        return retval

class Day:
    """
    """
    def __init__(self, day, mon, year):
        self.day  = day  # day of the month
        self.mon  = mon  # month of the year
        self.yh   = year // 100 # year hundred
        self.ys   = year %  100 # year - the last 2 digits

    def __str__(self): 
        return f'{cfg.WEEK_DAYS.get(self.wd_norm)} - {self.day}.{self.mon}.{self.year}'

    def __eq__(self, other):
        if self.day == other.day and self.mon == other.mon and self.year == other.year:
            return True
        else:
            return False
            
    def __lt__(self, other):
        o_year = other.year
        s_year = self.year
        if s_year < o_year:
            return True
        if s_year == o_year and self.mon < other.mon:
            return True
        if s_year == o_year and self.mon == other.mon and self.day < other.day:
            return True
        return False

    def __gt__(self, other):
        o_year = other.year
        s_year = self.year
        if s_year > o_year:
            return True
        if s_year == o_year and self.mon > other.mon:
            return True
        if s_year == o_year and self.mon == other.mon and self.day > other.day:
            return True
        return False

    def __sub__(self, other):
        test = copy.copy(other)
        diff = 0
        while self < test:
            test.decrement(1)
            diff -= 1
        while self > test:
            test.increment(1)
            diff += 1
        return diff

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
                    if (self.ys < 99):
                        self.ys += 1
                    else:
                        self.ys = 0
                        self.yh += 1                
                daysOfMonth = self.daysOfMonth
        return self

    def decrement(self, daysToSub):
        for ii in range(daysToSub):
            if(self.day > 1):
                self.day -= 1
            else:
                if (self.mon > 1):
                    self.mon -= 1
                else:
                    self.mon = 12
                    if (self.ys > 1):
                        self.ys -= 1
                    else:
                        self.ys = 99
                        self.yh -= 1                
                self.day = self.daysOfMonth
        return self

    @property
    def year(self):
        return self.yh * 100 + self.ys

    @property
    def __wd__(self):
        """
        weekDay in format So: 1, Mo: 2, Di: 3, Mi: 4, Do: 5, Fr: 6, Sa: 0
        """
        mon  = self.mon
        year = self.ys

        # Month to convert after Zeller - jan, feb will be 13 & 14 month of the year before
        if ( (mon == 1) or (mon == 2) ):
            mon  = mon  + 12
            year = year - 1
        
        # Weekday calculation after Christian Zeller
        # Sa: 0, So: 1, Mo: 2, Di: 3, Mi: 4, Do: 5, Fr: 6

        aktWoTag = (self.day + int(((mon+1)*26)/10) + year + int(year/4) + int(self.yh/4) - 2*self.yh) % 7
        aktWoTag = aktWoTag + 7 if (aktWoTag < 0) else aktWoTag
        
        return aktWoTag

    @property
    def wd_norm(self):
        wd = self.__wd__
        wd = wd + 7 if wd < 2 else wd 
        wd -= 2
        return wd

    @property
    def weekday(self):
        return cfg.WEEK_DAYS[self.wd_norm]

    @property
    def weekdayShort(self):
        return cfg.WEEK_DAYS[self.wd_norm][0:2]
    
    @property
    def cw(self):
        moCw1 = getMoCw1(self.year)
        days = self - moCw1
        week = int(days / 7)
        if days < 0:
            weeksOfLastYear = Day(1, 1, self.year).decrement(1).cw
            week += weeksOfLastYear
        else:
            week += 1
        return week

    @property
    def daysOfMonth(self):
        return getDaysPerMonth(self.mon, self.yh, self.ys)

    def incToWeekDay(self, nextWeekDay):
        """
        Increments to the next day of the week.

        weekDay in format So: 1, Mo: 2, Di: 3, Mi: 4, Do: 5, Fr: 6, Sa: 0
        """

        currentWeekDay = self.__wd__

        if( nextWeekDay > currentWeekDay ):
            self.increment(nextWeekDay - currentWeekDay)
            #printf("aktW: %i, gesW: %i -> %i tage addiern\n",aktWoTag,sWoTag,sWoTag-aktWoTag);
        if( nextWeekDay < currentWeekDay ):
            self.increment(7 - currentWeekDay + nextWeekDay)
            #printf("aktW: %i, gesW: %i -> %i tage addiern\n",aktWoTag,sWoTag,7-aktWoTag+sWoTag);

class SpecialDay(Day):
    def __init__(self, day=1, mon=1, year=0, name='', offset=0, incToWeekDay=-1):

        if isinstance(day, Day):
            super(SpecialDay, self).__init__(day.day, day.mon, day.year)
        else:
            super(SpecialDay, self).__init__(day, mon, year)
        
        self.name = name
        
        if offset > 0:
            self.increment(offset)
        elif offset < 0:
            self.decrement(-offset)
        
        if not incToWeekDay == -1:
            self.incToWeekDay(incToWeekDay)

    def __str__(self):
        dtype = ''
        if self.type == SpecialDayType.IGNORE:
            dtype = "ignored"
        if self.type == SpecialDayType.INFO_DAY:
            dtype = "info"
        if self.type == SpecialDayType.HOLIDAY:
            dtype = "holiday"
 
        return f'{cfg.WEEK_DAYS.get(self.wd_norm)} - {self.day}.{self.mon}.{self.year}{self.ys} - {self.name} - {dtype}' 

    @property
    def name(self):
        return(cfg.TRANSLATE_DAY[self._name]['name'])

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        return(cfg.TRANSLATE_DAY[self._name]['type'])

def getEaster(yh, ys):

    # Berechnung nach Christian Zeller
    
    a = (5 * yh + ys) % 19
    g = yh - int(yh / 4) - int(((8 * yh) + 13) / 25)
    b = ((19 * a) + 15 + g) % 30
    d = (b + ys + int(ys/4) + int(yh/4) + 2 - (2 * yh)) % 7
    d = d + 7 if ( d < 0 ) else d
    # Sonderfallbehandlung
    if( ((d == 0) and (b == 29)) or ((d == 0) and (b == 28) and (a > 10)) ):
        d = 7
    daysAfter21M = b + 7 - int(d)
    
    # Obige Formeln bestimmen wieviele Tage Ostersonntag nach dem 21.3 ist
    year = yh * 100 + ys
    easter = Day(21, 3, year)
    easter.increment(daysAfter21M)

    return easter

def getMoCw1(year):
    tmp = Day( 1,  1, year) # needed for Calender week - ISO 8601
    tmp.incToWeekDay(5) # Thursday is always CW 1
    tmp.decrement(3) # now tmp is Monday CW1
    return tmp

def getDaysPerMonth(mon, yh, ys):

    if not (mon == 2):
        d = DAYS_PER_MONTH.get(mon)
    else:
        if((ys % 4) == 0): # wenn das jahr durch 4 teilbar ist schaltjahr
            d = 29
            if(ys == 0): # außer volles yh
                d = 28
                if((yh % 4) == 0): # ausnahme der ausnahme: yh durch 4 teilbar
                    d = 29
        else:
            d = 28
    return d
