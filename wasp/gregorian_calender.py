# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2021 Andreas Lefevre

"""Calender
~~~~~~~~~~~

Shows special days.

For calculation the calender formulas of Christian Zeller will be used.
"""

# Dictionary for the number of days per month - note the missing february
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
    """ Can be used like an enumeration for weekdays 
    """
    MONDAY    = 0
    TUESDAY   = 1
    WEDNESDAY = 2
    THURSDAY  = 3
    FRIDAY    = 4
    SATURDAY  = 5
    SUNDAY    = 6

class SpecialDayType():
    """ Can be used like an enumeration for special days
        SpecialDayType is used to declare a day important in the cfg e.g. gregorian_calender_cfg_uk.py
    """
    IGNORE   = 0
    INFO_DAY = 1
    HOLIDAY  = 2

# Dictionary for colors used by dayColors
colors = {'white'  : 0xffff,
          'red'    : 0xf800,
          'yellow' : 0xffe0,
          'green'  : 0x07e0, 
          'cyan'   : 0x07ff,
          'blue'   : 0xffff,
          'magenta': 0xf81f}

# Defines a color for an *Special Day*
dayColors = {'sunday'  : colors['red'],
             'holiday' : colors['magenta'],
             'infoday' : colors['cyan']}

import copy
import gregorian_calender_cfg_uk as cfg

try:
    import machine
except:
    pass

class Year:
    _instance = None

    def __new__(cls, year):
        if cls._instance is None:
            # Creating the object for Year - Singleton
            # see https://python-patterns.guide/gang-of-four/singleton/
            cls._instance = super(Year, cls).__new__(cls)
            # Put any initialization here.
            cls.specialDays = dict()
            cls._year = -1
        return cls._instance

    def __init__(self, year):
        if(self._year != year):
            print(f'Year: Change the year to {year}')
            try:
                t = machine.Timer(id=1, period=8000000)
                t.start()
            except:
                pass
            self._year = year
            self._update()
            try:
                elapsed = t.time()
                t.stop()
                del t
                print('took {}s'.format(elapsed / 1000000))
            except:
                pass
 
    def __str__(self):
        return f'{self._year}'

    @property
    def year(self):
        return self._year

    def _addSpecialDay(self, specialDay):
        self.specialDays[specialDay._name] = specialDay

    def _update(self):
        yh   = self.year // 100 # year hundred
        ys   = self.year %  100 # year - the last 2 digits

        easter = getEaster(yh, ys)
        ref1 = Day(27, 11, self.year) # needed for 1. Advent
        ref2 = Day( 1,  5, self.year) # needed for Muttertag
        ref3 = Day(23, 11, self.year) # needed for Buß und Bettag
        ref4 = Day( 1, 10, self.year) # needed for Erntedank
        ref5 = Day( 1,  4, self.year) # needed for Sommerzeit
        ref6 = Day( 1, 11, self.year) # needed for Normalzeit


        self._addSpecialDay(SpecialDay(name="Women's Shrovetide",   day=easter, offset= -52))
        self._addSpecialDay(SpecialDay(name="Carnival Monday",      day=easter, offset= -48)) 
        self._addSpecialDay(SpecialDay(name="Shrove Tuesday",       day=easter, offset= -47)) 
        self._addSpecialDay(SpecialDay(name="Ash Wednesday",        day=easter, offset= -46)) 
        self._addSpecialDay(SpecialDay(name="Palm Sunday",          day=easter, offset=  -7))
        self._addSpecialDay(SpecialDay(name="Maundy Thursday",      day=easter, offset=  -3)) 
        self._addSpecialDay(SpecialDay(name="Good Friday",          day=easter, offset=  -2)) 
        self._addSpecialDay(SpecialDay(name="Holy Saturday",        day=easter, offset=  -1)) 
        self._addSpecialDay(SpecialDay(name="Easter Sunday",        day=easter))              
        self._addSpecialDay(SpecialDay(name="Easter Monday",        day=easter, offset=   1)) 
        self._addSpecialDay(SpecialDay(name="White Sunday",         day=easter, offset=   7)) 
        self._addSpecialDay(SpecialDay(name="Fathers day (de)",     day=easter, offset=  39)) 
        self._addSpecialDay(SpecialDay(name="Ascension of Christ",  day=easter, offset=  39)) 
        self._addSpecialDay(SpecialDay(name="Pentecost Sunday",     day=easter, offset=  49)) 
        self._addSpecialDay(SpecialDay(name="Whit Monday",          day=easter, offset=  50)) 
        self._addSpecialDay(SpecialDay(name="Corpus Christi",       day=easter, offset=  60)) 
        
        self._addSpecialDay(SpecialDay(name="Memorial Day (de)", day=ref1, offset=-14, incToWeekDay=WeekDayNorm.SUNDAY))
        self._addSpecialDay(SpecialDay(name="1 Advent",          day=ref1, incToWeekDay=WeekDayNorm.SUNDAY))            
        self._addSpecialDay(SpecialDay(name="2 Advent",          day=ref1, offset=7, incToWeekDay=WeekDayNorm.SUNDAY))  
        self._addSpecialDay(SpecialDay(name="3 Advent",          day=ref1, offset=14, incToWeekDay=WeekDayNorm.SUNDAY)) 
        self._addSpecialDay(SpecialDay(name="4 Advent",          day=ref1, offset=21, incToWeekDay=WeekDayNorm.SUNDAY)) 

        self._addSpecialDay(SpecialDay(name="Mother's Day (de,us)",      day=ref2, offset=7, incToWeekDay=WeekDayNorm.SUNDAY)) 
        
        self._addSpecialDay(SpecialDay(name="Thanksgiving (de)", day=ref4, incToWeekDay=WeekDayNorm.SUNDAY)) 

        self._addSpecialDay(SpecialDay(name="Buß- und Bettag",   day=ref3, offset=-7, incToWeekDay=WeekDayNorm.WEDNESDAY )) 
        
        self._addSpecialDay(SpecialDay(name="Summertime (eu)",   day=ref5, offset= -7, incToWeekDay=WeekDayNorm.SUNDAY))
        self._addSpecialDay(SpecialDay(name="Normaltime (eu)",   day=ref6, offset= -7, incToWeekDay=WeekDayNorm.SUNDAY)) 

        
        self._addSpecialDay(SpecialDay(name="New Year",                      day= 1, mon= 1, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Holy three kings",              day= 6, mon= 1, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Valentine's day",               day=14, mon= 2, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Women's Day",                   day= 8, mon= 3, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="March equinox",                 day=20, mon= 3, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Day of the beer",               day=23, mon= 4, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Labor Day (de)",                day= 1, mon= 5, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Europe day",                    day= 5, mon= 5, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Victory in Europe",             day= 8, mon= 5, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Constitution (de)",             day=23, mon= 5, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Popular uprising DDR 1953",     day=17, mon= 6, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Summer solstice",               day=21, mon= 6, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Attack 1944",                   day=20, mon= 7, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Peace Festival Augsburg",       day= 8, mon= 8, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Assumption Day",                day=15, mon= 8, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Children's Day",                day=20, mon= 9, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="September equinox",             day=23, mon= 9, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Begin WW2 1939",                day= 1, mon=10, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Day of German unity",           day= 3, mon=10, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Hiroshima 1945",                day= 6, mon=10, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Construction of the wall 1961", day=13, mon=10, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Reformation Day 1517",          day=31, mon=10, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="All Saints Day",                day= 1, mon=11, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="All Souls Day",                 day= 2, mon=11, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="October Revolution 1917",       day= 7, mon=11, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="9. November (Germany)",         day= 9, mon=11, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="St. Nicholas Day",              day= 6, mon=12, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Mary Conception",               day= 8, mon=12, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Martin's Day" ,                 day=11, mon=11, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Winter solstice",               day=22, mon=12, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Christmas eve" ,                day=24, mon=12, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="First christmasday",            day=25, mon=12, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="Second christmasday",           day=26, mon=12, year=self.year)) 
        self._addSpecialDay(SpecialDay(name="New Year's Eve",                day=31, mon=12, year=self.year)) 

        # see https://en.wikipedia.org/wiki/Public_and_bank_holidays_in_Scotland
        # The holiday on 1 January (or 2 January if 1 January is Sunday) is statutory. If New Year's Day is Saturday a 
        # substitute holiday is given on 4 January by Royal Proclamation. 2 January is given by Royal Proclamation, with 
        # a substitute holiday on 4 January if it is Saturday and 3 January if it is Sunday or Monday. 
        if self.specialDays["New Year"].wd_norm == WeekDayNorm.SATURDAY or self.specialDays["New Year"].wd_norm == WeekDayNorm.SUNDAY:
            self._addSpecialDay(SpecialDay(name="New Year observed (uk)", day= 1, mon= 1, year=self.year, incToWeekDay=WeekDayNorm.MONDAY)) 
            secoundJan = copy.copy(self.specialDays["New Year observed (uk)"]).increment(1)
        else:
            secoundJan = copy.copy(self.specialDays["New Year"]).increment(1)
        secoundJan.name = "2nd January (Scotland)"

        if secoundJan.wd_norm == WeekDayNorm.SATURDAY or secoundJan.wd_norm == WeekDayNorm.SUNDAY:
            secoundJan.incToWeekDay(WeekDayNorm.MONDAY)
        self._addSpecialDay(secoundJan)

        self._addSpecialDay(SpecialDay(name="St Patrick's Day",  day=17, mon=3, year=self.year)) 
        if self.specialDays["St Patrick's Day"].wd_norm == WeekDayNorm.SATURDAY or self.specialDays["St Patrick's Day"].wd_norm == WeekDayNorm.SUNDAY:
            self._addSpecialDay(SpecialDay(name="St Patrick's Day observed (ni)", day= 17, mon= 3, year=self.year, incToWeekDay=WeekDayNorm.MONDAY)) 

        self._addSpecialDay(SpecialDay(name="St. David's Day",  day=1, mon=3, year=self.year)) 

        # see https://en.wikipedia.org/wiki/Saint_George%27s_Day
        # no saints' day should be celebrated between Palm Sunday and the Sunday after Easter Day so if 23 April falls 
        # in that period the celebrations are transferred to after it.
        saintGeorgesDay = SpecialDay(name="Saint George's Day", day= 23, mon= 4, year=self.year)        
        if not saintGeorgesDay < self.specialDays["Palm Sunday"]:
            while not saintGeorgesDay > self.specialDays["White Sunday"]:
                saintGeorgesDay.increment(1)
        self._addSpecialDay(saintGeorgesDay) 

        self._addSpecialDay(SpecialDay(name="Shakespeare Day",  day=23, mon=4, year=self.year)) 

        # in 1995 this holiday was moved to Monday 8 May and in 2020 to Friday 8 May – to commemorate the 50th and 75th anniversary of VE Day.
        if self.year == 1995 or self.year == 2020:
            self._addSpecialDay(SpecialDay(name="Early May Bank Holiday",  day=8, mon=5, year=self.year)) 
        else:
            self._addSpecialDay(SpecialDay(name="Early May Bank Holiday",  day=1, mon=5, year=self.year, incToWeekDay=WeekDayNorm.MONDAY)) 
        
        # see Queen's Platinum Jubilee in 2022 https://www.bbc.com/news/uk-54911550
        if self.year == 2022:
            self._addSpecialDay(SpecialDay(name="Spring Bank Holiday",  day=2, mon=6, year=self.year)) 
            self._addSpecialDay(SpecialDay(name="Queen's Platinum Jubilee",  day=3, mon=6, year=self.year)) 
        else:
            self._addSpecialDay(SpecialDay(name="Spring Bank Holiday",  day=31, mon=5, year=self.year, offset=-6, incToWeekDay=WeekDayNorm.MONDAY)) 

        #  Queen's Official Birthday celebrated on the second Saturday of June see https://en.wikipedia.org/wiki/Queen%27s_Official_Birthday
        self._addSpecialDay(SpecialDay(name="Queen's Official Birthday",  day=1, mon=6, year=self.year, offset=7, incToWeekDay=WeekDayNorm.SATURDAY)) 

        #  It is celebrated in Canada, the United Kingdom, and the United States on the third Sunday of June
        self._addSpecialDay(SpecialDay(name="Father's Day (uk, us , ca)",  day=1, mon=6, year=self.year, offset=14, incToWeekDay=WeekDayNorm.SUNDAY)) 

        self._addSpecialDay(SpecialDay(name="Halloween",  day=31, mon=10, year=self.year)) 

        bOTB = SpecialDay(name="Battle of the Boyne (ni)",  day=12, mon=7, year=self.year)
        self._addSpecialDay(bOTB) 
        if bOTB.wd_norm == WeekDayNorm.SATURDAY or bOTB.wd_norm == WeekDayNorm.SUNDAY:
            self._addSpecialDay(SpecialDay(name="Battle of the Boyne observed (ni)",  day=12, mon=7, year=self.year, incToWeekDay=WeekDayNorm.MONDAY)) 
        
        self._addSpecialDay(SpecialDay(name="June Bank Holiday (ir)",            day=1, mon=6, year=self.year, incToWeekDay=WeekDayNorm.MONDAY)) 
        self._addSpecialDay(SpecialDay(name="Summer Bank Holiday (sc)",          day=1, mon=8, year=self.year, incToWeekDay=WeekDayNorm.MONDAY)) 
        self._addSpecialDay(SpecialDay(name="Summer Bank Holiday (eng,ni,wal)",  day=1, mon=9, year=self.year, offset=-7, incToWeekDay=WeekDayNorm.MONDAY)) 
         
        self._addSpecialDay(SpecialDay(name="Mother's Day (uk)",          day=easter, offset=  -21))
        self._addSpecialDay(SpecialDay(name="Guy Fawkes Day",             day=5, mon=11, year=self.year))
        self._addSpecialDay(SpecialDay(name="Remembrance Sunday",         day=1, mon=11, year=self.year, offset=7, incToWeekDay=WeekDayNorm.SUNDAY))

        self._addSpecialDay(SpecialDay(name="St Andrew's Day",         day=30, mon=11, year=self.year))
        if self.specialDays["St Andrew's Day"].wd_norm == WeekDayNorm.SATURDAY or self.specialDays["St Andrew's Day"].wd_norm == WeekDayNorm.SUNDAY:
            self._addSpecialDay(SpecialDay(name="St Andrew's Day observed (sc)", day= 30, mon= 11, year=self.year, incToWeekDay=WeekDayNorm.MONDAY)) 
 
        # If Boxing Day falls on a Saturday, the following Monday is a substitute bank holiday. 
        # If Christmas Day falls on a Saturday, the following Monday and Tuesday are substitute bank holidays.
        if self.specialDays["First christmasday"].wd_norm == WeekDayNorm.SATURDAY:
            self._addSpecialDay(SpecialDay(name="Christmas Day observed (uk)", day= 25, mon= 12, year=self.year, incToWeekDay=WeekDayNorm.MONDAY)) 
            self._addSpecialDay(SpecialDay(name="Boxing Day observed (uk)", day= 25, mon= 12, year=self.year, incToWeekDay=WeekDayNorm.TUESDAY)) 
        elif self.specialDays["Second christmasday"].wd_norm == WeekDayNorm.SATURDAY:
            self._addSpecialDay(SpecialDay(name="Boxing Day observed (uk)", day= 25, mon= 12, year=self.year, incToWeekDay=WeekDayNorm.MONDAY)) 

        self._addSpecialDay(SpecialDay(name="Birthday of Martin Luther King, Jr", day=15, mon= 1, year=self.year, incToWeekDay=WeekDayNorm.MONDAY))
        self._addSpecialDay(SpecialDay(name="Washington's Birthday",              day=15, mon= 2, year=self.year, incToWeekDay=WeekDayNorm.MONDAY))
        self._addSpecialDay(SpecialDay(name="Memorial Day (us)",                  day=25, mon= 5, year=self.year, incToWeekDay=WeekDayNorm.MONDAY))

        # If July 4 is a Saturday, it is observed on Friday, July 3. If July 4 is a Sunday, it is observed on Monday, July 5
        self._addSpecialDay(SpecialDay(name="US Independence Day",                day= 4, mon= 7, year=self.year))
        if self.specialDays["US Independence Day"].wd_norm == WeekDayNorm.SATURDAY:
            self._addSpecialDay(SpecialDay(name="US Independence Day observed", day= 4, mon= 7, year=self.year, offset=-1)) 
        if self.specialDays["US Independence Day"].wd_norm == WeekDayNorm.SUNDAY:
            self._addSpecialDay(SpecialDay(name="US Independence Day observed", day= 4, mon= 7, year=self.year, offset=1)) 

        self._addSpecialDay(SpecialDay(name="Labor Day (us)",                     day= 1, mon= 9, year=self.year, incToWeekDay=WeekDayNorm.MONDAY))
        self._addSpecialDay(SpecialDay(name="Columbus Day",                       day= 8, mon=10, year=self.year, incToWeekDay=WeekDayNorm.MONDAY))

        # If Veterans Day falls on a Saturday, they are closed on Friday November 10. If Veterans Day falls on a Sunday, they are closed on Monday November 12.
        self._addSpecialDay(SpecialDay(name="Veterans Day (us)",                  day=11, mon=11, year=self.year))
        if self.specialDays["Veterans Day (us)"].wd_norm == WeekDayNorm.SATURDAY:
            self._addSpecialDay(SpecialDay(name="Veterans Day (us) observed", day=11, mon=11, year=self.year, offset=-1)) 
        if self.specialDays["Veterans Day (us)"].wd_norm == WeekDayNorm.SUNDAY:
            self._addSpecialDay(SpecialDay(name="Veterans Day (us) observed", day=11, mon=11, year=self.year, offset=1)) 

        self._addSpecialDay(SpecialDay(name="Thanksgiving (us)", day=22, mon=11, year=self.year, incToWeekDay=WeekDayNorm.THURSDAY))
        self._addSpecialDay(SpecialDay(name="Juneteenth (us)",   day=19, mon= 6, year=self.year))
 
    def specialDayList(self, day, mon):
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
    def wd_norm(self):
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
        
        return convertZellerWdToNormWd(aktWoTag)

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
        """
        currentWeekDay = self.wd_norm

        if( nextWeekDay > currentWeekDay ):
            self.increment(nextWeekDay - currentWeekDay)
        if( nextWeekDay < currentWeekDay ):
            self.increment(7 - currentWeekDay + nextWeekDay)

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
    tmp.incToWeekDay(WeekDayNorm.THURSDAY) # Thursday is always CW 1
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

def convertZellerWdToNormWd(zellerWd):
    # from weekDay in format  Sa: 0, So: 1, Mo: 2, Di: 3, Mi: 4, Do: 5, Fr: 6
    # to WeekDayNorm()                      Mo: 0, Di: 1, Mi: 2, Do: 3, Fr: 4, Sa: 5, So: 6,
    wd = zellerWd
    wd = wd + 7 if wd < 2 else wd 
    wd -= 2
    return wd    

def convertNormWdToZellerWd(normWd):
    # from WeekDayNorm():                 Mo: 0, Di: 1, Mi: 2, Do: 3, Fr: 4, Sa: 5, So: 6,
    # to weekDay in format  Sa: 0, So: 1, Mo: 2, Di: 3, Mi: 4, Do: 5, Fr: 6
    wd = normWd
    wd += 2
    wd = wd + 7 if wd > 6 else wd 
    return wd
