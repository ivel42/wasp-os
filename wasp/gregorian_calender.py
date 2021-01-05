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
                   8: 31,
                   9: 30,
                  10: 31,
                  11: 30,
                  12: 31}

class WeekDayNorm():
    MONDAY    = 0
    TUESDAY   = 1
    WEDNESDAY = 2
    THURSDAY  = 3
    FRIDAY    = 4
    SATURDAY  = 5
    SUNDAY    = 6

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
        self.addSpecialDay(SpecialDay(name="Fathers day (de)",     day=self.easter, offset=  39)) 
        self.addSpecialDay(SpecialDay(name="Ascension of Christ",  day=self.easter, offset=  39)) 
        self.addSpecialDay(SpecialDay(name="Pentecost Sunday",     day=self.easter, offset=  49)) 
        self.addSpecialDay(SpecialDay(name="Whit Monday",          day=self.easter, offset=  50)) 
        self.addSpecialDay(SpecialDay(name="Corpus Christi",       day=self.easter, offset=  60)) 

        self.addSpecialDay(SpecialDay(name="Memorial Day (de)", day=self.ref1, offset=-14, incToWeekDay=1))
        self.addSpecialDay(SpecialDay(name="1 Advent",          day=self.ref1, incToWeekDay=1))            
        self.addSpecialDay(SpecialDay(name="2 Advent",          day=self.ref1, offset=7, incToWeekDay=1))  
        self.addSpecialDay(SpecialDay(name="3 Advent",          day=self.ref1, offset=14, incToWeekDay=1)) 
        self.addSpecialDay(SpecialDay(name="4 Advent",          day=self.ref1, offset=21, incToWeekDay=1)) 

        self.addSpecialDay(SpecialDay(name="Mother's Day (de,us)",      day=self.ref2, offset=7, incToWeekDay=1)) 
        
        self.addSpecialDay(SpecialDay(name="Thanksgiving (de)", day=self.ref4, incToWeekDay=1)) 

        self.addSpecialDay(SpecialDay(name="Buß- und Bettag",   day=self.ref3, offset=-7, incToWeekDay=4)) 
        
        self.addSpecialDay(SpecialDay(name="Summertime (eu)",   day=self.ref5, offset= -7, incToWeekDay=1))
        self.addSpecialDay(SpecialDay(name="Normaltime (eu)",   day=self.ref6, offset= -7, incToWeekDay=1)) 

        
        self.addSpecialDay(SpecialDay(name="New Year",                      day= 1, mon= 1, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Holy three kings",              day= 6, mon= 1, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Valentine's day",               day=14, mon= 2, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Women's Day",                   day= 8, mon= 3, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="March equinox",                 day=20, mon= 3, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Day of the beer",               day=23, mon= 4, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Labor Day (de)",                day= 1, mon= 5, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Europe day",                    day= 5, mon= 5, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Victory in Europe",             day= 8, mon= 5, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Constitution (de)",             day=23, mon= 5, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Popular uprising DDR 1953",     day=17, mon= 6, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Summer solstice",               day=21, mon= 6, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Attack 1944",                   day=20, mon= 7, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Peace Festival Augsburg",       day= 8, mon= 8, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Assumption Day",                day=15, mon= 8, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Children's Day",                day=20, mon= 9, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="September equinox",             day=23, mon= 9, year=self.year)) 
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

        # see https://en.wikipedia.org/wiki/Public_and_bank_holidays_in_Scotland
        # The holiday on 1 January (or 2 January if 1 January is Sunday) is statutory. If New Year's Day is Saturday a 
        # substitute holiday is given on 4 January by Royal Proclamation. 2 January is given by Royal Proclamation, with 
        # a substitute holiday on 4 January if it is Saturday and 3 January if it is Sunday or Monday. 
        if self.specialDays["New Year"].wd_norm == WeekDayNorm.SATURDAY or self.specialDays["New Year"].wd_norm == WeekDayNorm.SUNDAY:
            self.addSpecialDay(SpecialDay(name="New Year observed (uk)", day= 1, mon= 1, year=self.year, incToWeekDay=2)) 
            secoundJan = copy.copy(self.specialDays["New Year observed (uk)"]).increment(1)
        else:
            secoundJan = copy.copy(self.specialDays["New Year"]).increment(1)
        secoundJan.name = "2nd January (Scotland)"

        if secoundJan.wd_norm == WeekDayNorm.SATURDAY or secoundJan.wd_norm == WeekDayNorm.SUNDAY:
            secoundJan.incToWeekDay(2)
        self.addSpecialDay(secoundJan)

        self.addSpecialDay(SpecialDay(name="St Patrick's Day",  day=17, mon=3, year=self.year)) 
        if self.specialDays["St Patrick's Day"].wd_norm == WeekDayNorm.SATURDAY or self.specialDays["St Patrick's Day"].wd_norm == WeekDayNorm.SUNDAY:
            self.addSpecialDay(SpecialDay(name="St Patrick's Day observed (ni)", day= 17, mon= 3, year=self.year, incToWeekDay=2)) 

        self.addSpecialDay(SpecialDay(name="St. David's Day",  day=1, mon=3, year=self.year)) 

        # see https://en.wikipedia.org/wiki/Saint_George%27s_Day
        # no saints' day should be celebrated between Palm Sunday and the Sunday after Easter Day so if 23 April falls 
        # in that period the celebrations are transferred to after it.
        saintGeorgesDay = SpecialDay(name="Saint George's Day", day= 23, mon= 4, year=self.year)        
        if not saintGeorgesDay < self.specialDays["Palm Sunday"]:
            while not saintGeorgesDay > self.specialDays["White Sunday"]:
                saintGeorgesDay.increment(1)
        self.addSpecialDay(saintGeorgesDay) 

        self.addSpecialDay(SpecialDay(name="Shakespeare Day",  day=23, mon=4, year=self.year)) 

        # in 1995 this holiday was moved to Monday 8 May and in 2020 to Friday 8 May – to commemorate the 50th and 75th anniversary of VE Day.
        if self.year == 1995 or self.year == 2020:
            self.addSpecialDay(SpecialDay(name="Early May Bank Holiday",  day=8, mon=5, year=self.year)) 
        else:
            self.addSpecialDay(SpecialDay(name="Early May Bank Holiday",  day=1, mon=5, year=self.year, incToWeekDay=2)) 
        
        # see Queen's Platinum Jubilee in 2022 https://www.bbc.com/news/uk-54911550
        if self.year == 2022:
            self.addSpecialDay(SpecialDay(name="Spring Bank Holiday",  day=2, mon=6, year=self.year)) 
            self.addSpecialDay(SpecialDay(name="Queen's Platinum Jubilee",  day=3, mon=6, year=self.year)) 
        else:
            self.addSpecialDay(SpecialDay(name="Spring Bank Holiday",  day=31, mon=5, year=self.year, offset=-6, incToWeekDay=2)) 

        #  Queen's Official Birthday celebrated on the second Saturday of June see https://en.wikipedia.org/wiki/Queen%27s_Official_Birthday
        self.addSpecialDay(SpecialDay(name="Queen's Official Birthday",  day=1, mon=6, year=self.year, offset=7, incToWeekDay=0)) 

        #  It is celebrated in Canada, the United Kingdom, and the United States on the third Sunday of June
        self.addSpecialDay(SpecialDay(name="Father's Day (uk, us , ca)",  day=1, mon=6, year=self.year, offset=14, incToWeekDay=1)) 

        self.addSpecialDay(SpecialDay(name="Halloween",  day=31, mon=10, year=self.year)) 

        bOTB = SpecialDay(name="Battle of the Boyne (ni)",  day=12, mon=7, year=self.year)
        self.addSpecialDay(bOTB) 
        if bOTB.wd_norm == WeekDayNorm.SATURDAY or bOTB.wd_norm == WeekDayNorm.SUNDAY:
            self.addSpecialDay(SpecialDay(name="Battle of the Boyne observed (ni)",  day=12, mon=7, year=self.year, incToWeekDay=2)) 
        
        self.addSpecialDay(SpecialDay(name="June Bank Holiday (ir)",            day=1, mon=6, year=self.year, incToWeekDay=2)) 
        self.addSpecialDay(SpecialDay(name="Summer Bank Holiday (sc)",          day=1, mon=8, year=self.year, incToWeekDay=2)) 
        self.addSpecialDay(SpecialDay(name="Summer Bank Holiday (eng,ni,wal)",  day=1, mon=9, year=self.year, offset=-7, incToWeekDay=2)) 
         
        self.addSpecialDay(SpecialDay(name="Mother's Day (uk)",          day=self.easter, offset=  -21))
        self.addSpecialDay(SpecialDay(name="Guy Fawkes Day",             day=5, mon=11, year=self.year))
        self.addSpecialDay(SpecialDay(name="Remembrance Sunday",         day=1, mon=11, year=self.year, offset=7, incToWeekDay=1))

        self.addSpecialDay(SpecialDay(name="St Andrew's Day",         day=30, mon=11, year=self.year))
        if self.specialDays["St Andrew's Day"].wd_norm == WeekDayNorm.SATURDAY or self.specialDays["St Andrew's Day"].wd_norm == WeekDayNorm.SUNDAY:
            self.addSpecialDay(SpecialDay(name="St Andrew's Day observed (sc)", day= 30, mon= 11, year=self.year, incToWeekDay=2)) 
 
        # If Boxing Day falls on a Saturday, the following Monday is a substitute bank holiday. 
        # If Christmas Day falls on a Saturday, the following Monday and Tuesday are substitute bank holidays.
        if self.specialDays["First christmasday"].wd_norm == WeekDayNorm.SATURDAY:
            self.addSpecialDay(SpecialDay(name="Christmas Day observed (uk)", day= 25, mon= 12, year=self.year, incToWeekDay=2)) 
            self.addSpecialDay(SpecialDay(name="Boxing Day observed (uk)", day= 25, mon= 12, year=self.year, incToWeekDay=3)) 
        elif self.specialDays["Second christmasday"].wd_norm == WeekDayNorm.SATURDAY:
            self.addSpecialDay(SpecialDay(name="Boxing Day observed (uk)", day= 25, mon= 12, year=self.year, incToWeekDay=2)) 

        self.addSpecialDay(SpecialDay(name="Birthday of Martin Luther King, Jr", day=15, mon= 1, year=self.year, incToWeekDay=2))
        self.addSpecialDay(SpecialDay(name="Washington's Birthday",              day=15, mon= 2, year=self.year, incToWeekDay=2))
        self.addSpecialDay(SpecialDay(name="Memorial Day (us)",                  day=25, mon= 5, year=self.year, incToWeekDay=2))

        # If July 4 is a Saturday, it is observed on Friday, July 3. If July 4 is a Sunday, it is observed on Monday, July 5
        self.addSpecialDay(SpecialDay(name="US Independence Day",                day= 4, mon= 7, year=self.year))
        if self.specialDays["US Independence Day"].wd_norm == WeekDayNorm.SATURDAY:
            self.addSpecialDay(SpecialDay(name="US Independence Day observed", day= 4, mon= 7, year=self.year, offset=-1)) 
        if self.specialDays["US Independence Day"].wd_norm == WeekDayNorm.SUNDAY:
            self.addSpecialDay(SpecialDay(name="US Independence Day observed", day= 4, mon= 7, year=self.year, offset=1)) 

        self.addSpecialDay(SpecialDay(name="Labor Day (us)",                     day= 1, mon= 9, year=self.year, incToWeekDay=2))
        self.addSpecialDay(SpecialDay(name="Columbus Day",                       day= 8, mon=10, year=self.year, incToWeekDay=2))

        # If Veterans Day falls on a Saturday, they are closed on Friday November 10. If Veterans Day falls on a Sunday, they are closed on Monday November 12.
        self.addSpecialDay(SpecialDay(name="Veterans Day (us)",                  day=11, mon=11, year=self.year))
        if self.specialDays["Veterans Day (us)"].wd_norm == WeekDayNorm.SATURDAY:
            self.addSpecialDay(SpecialDay(name="Veterans Day (us) observed", day=11, mon=11, year=self.year, offset=-1)) 
        if self.specialDays["Veterans Day (us)"].wd_norm == WeekDayNorm.SUNDAY:
            self.addSpecialDay(SpecialDay(name="Veterans Day (us) observed", day=11, mon=11, year=self.year, offset=1)) 

        self.addSpecialDay(SpecialDay(name="Thanksgiving (us)", day=22, mon=11, year=self.year, incToWeekDay=5))
        self.addSpecialDay(SpecialDay(name="Juneteenth (us)",   day=19, mon= 6, year=self.year))
 
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
        if self._name in cfg.TRANSLATE_DAY:
            return(cfg.TRANSLATE_DAY[self._name]['name'])
        else:
            return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        if self._name in cfg.TRANSLATE_DAY:
            return(cfg.TRANSLATE_DAY[self._name]['type'])
        else:
            return SpecialDayType.IGNORE

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
