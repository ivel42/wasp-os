# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2021 Andreas Lefevre

"""Calender
~~~~~~~~~~~

Shows special days.

For calculation the calender formulas of Christian Zeller will be used.
"""

#import wasp
import copy

WEEK_DAYS_DE = {0: 'Samstag',
                1: 'Sonntag',
                2: 'Montag',
                3: 'Dienstag',
                4: 'Mittwoch',
                5: 'Donnerstag',
                6: 'Freitag'}

MONTH_NAMES_DE = {1: 'Januar',
                  2: 'Februar',
                  3: 'März',
                  4: 'April',
                  5: 'Mai',
                  6: 'Juni',
                  7: 'Juli',
                  8: 'August',
                  9: 'September',
                 10: 'Oktober',
                 11: 'November',
                 12: 'Dezember'}

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

TRANSLATE_US_DE = {
    "Women's Shrovetide"            : {"name" : "Weiberfastnacht"          , "type":SpecialDayType.INFO_DAY } ,       
    "Carnival Monday"               : {"name" : "Rosenmontag"              , "type":SpecialDayType.INFO_DAY } , 
    "Shrove Tuesday"                : {"name" : "Faschingsdienstag"        , "type":SpecialDayType.INFO_DAY } , 
    "Ash Wednesday"                 : {"name" : "Aschermittwoch"           , "type":SpecialDayType.INFO_DAY } , 
    "Palm Sunday"                   : {"name" : "Palmsonntag"              , "type":SpecialDayType.INFO_DAY } , 
    "Maundy Thursday"               : {"name" : "Gründonnerstag"           , "type":SpecialDayType.INFO_DAY } , 
    "Good Friday"                   : {"name" : "Karfreitag"               , "type":SpecialDayType.HOLIDAY  } , 
    "Holy Saturday"                 : {"name" : "Karsamstag"               , "type":SpecialDayType.INFO_DAY } , 
    "Easter Sunday"                 : {"name" : "Oster-Sonntag"            , "type":SpecialDayType.INFO_DAY } , 
    "Easter Monday"                 : {"name" : "Oster-Montag"             , "type":SpecialDayType.HOLIDAY  } , 
    "White Sunday"                  : {"name" : "Weißer Sonntag"           , "type":SpecialDayType.INFO_DAY } , 
    "Fathers day"                   : {"name" : "Vatertag"                 , "type":SpecialDayType.INFO_DAY } , 
    "Ascension of Christ"           : {"name" : "Christi Himmelfahrt"      , "type":SpecialDayType.HOLIDAY  } , 
    "Pentecost Sunday"              : {"name" : "Pfingstsonntag"           , "type":SpecialDayType.INFO_DAY } , 
    "Whit Monday"                   : {"name" : "Pfingstmontag"            , "type":SpecialDayType.HOLIDAY  } , 
    "Corpus Christi"                : {"name" : "Fronleichnam"             , "type":SpecialDayType.HOLIDAY  } , 
    "Memorial Day (de)"             : {"name" : "Volkstrauertag (de)"      , "type":SpecialDayType.INFO_DAY } ,           
    "1 Advent"                      : {"name" : "1. Advent"                , "type":SpecialDayType.INFO_DAY } ,        
    "2 Advent"                      : {"name" : "2. Advent"                , "type":SpecialDayType.INFO_DAY } , 
    "3 Advent"                      : {"name" : "3. Advent"                , "type":SpecialDayType.INFO_DAY } , 
    "4 Advent"                      : {"name" : "4. Advent"                , "type":SpecialDayType.INFO_DAY } , 
    "Mother's Day"                  : {"name" : "Muttertag"                , "type":SpecialDayType.INFO_DAY } , 
    "Thanksgiving (de)"             : {"name" : "Erntedank"                , "type":SpecialDayType.INFO_DAY } , 
    "Buß- und Bettag"               : {"name" : "Buß- und Bettag"          , "type":SpecialDayType.INFO_DAY } , 
    "Summertime (eu)"               : {"name" : "Sommerzeit von 2 zu 3"    , "type":SpecialDayType.INFO_DAY } ,  
    "Normaltime (eu)"               : {"name" : "Normalzeit von 3 zu 2"    , "type":SpecialDayType.INFO_DAY } ,    
    "New Year"                      : {"name" : "Neujahr"                  , "type":SpecialDayType.HOLIDAY  } ,  
    "Holy three kings"              : {"name" : "Hl. Drei Könige"          , "type":SpecialDayType.HOLIDAY  } ,  
    "Valentine's day"               : {"name" : "Valentinstag"             , "type":SpecialDayType.INFO_DAY } ,  
    "Women's Day"                   : {"name" : "Frauentag"                , "type":SpecialDayType.INFO_DAY } ,  
    "Day of the beer"               : {"name" : "Tag des Bieres"           , "type":SpecialDayType.INFO_DAY } ,  
    "Labor Day (de)"                : {"name" : "Tag der Arbeit (de)"      , "type":SpecialDayType.HOLIDAY  } ,  
    "Europe day"                    : {"name" : "Europatag"                , "type":SpecialDayType.INFO_DAY } ,  
    "Victory in Europe"             : {"name" : "Kriegsende 2. WK 1945"    , "type":SpecialDayType.INFO_DAY } ,  
    "Constitution (de)"             : {"name" : "Grundgesetz (de)"         , "type":SpecialDayType.INFO_DAY } ,  
    "Popular uprising DDR 1953"     : {"name" : "Volksaufstand DDR 1953"   , "type":SpecialDayType.INFO_DAY } ,  
    "Attack 1944"                   : {"name" : "Attentat 1944"            , "type":SpecialDayType.INFO_DAY } ,  
    "Summer solstice"               : {"name" : "Sommersonnenwende"        , "type":SpecialDayType.INFO_DAY } ,  
    "Peace Festival Augsburg"       : {"name" : "Friedensfest Augsburg"    , "type":SpecialDayType.INFO_DAY } ,  
    "Assumption Day"                : {"name" : "Mariä Himmelfahrt"        , "type":SpecialDayType.INFO_DAY } ,  
    "Children's Day"                : {"name" : "Kindertag"                , "type":SpecialDayType.INFO_DAY } ,  
    "Begin WW2 1939"                : {"name" : "Kriegsbeginn 2. WK 1939"  , "type":SpecialDayType.INFO_DAY } ,  
    "Day of German unity"           : {"name" : "Tag der Deutschen Einheit", "type":SpecialDayType.HOLIDAY  } ,  
    "Hiroshima 1945"                : {"name" : "Hiroshima 1945"           , "type":SpecialDayType.INFO_DAY } ,  
    "Construction of the wall 1961" : {"name" : "Mauerbau 1961"            , "type":SpecialDayType.INFO_DAY } ,  
    "Reformation Day 1517"          : {"name" : "Reformationstag 1517"     , "type":SpecialDayType.INFO_DAY } ,  
    "All Saints Day"                : {"name" : "Allerheiligen"            , "type":SpecialDayType.HOLIDAY  } ,  
    "All Souls Day"                 : {"name" : "Allerseelen"              , "type":SpecialDayType.INFO_DAY } ,  
    "October Revolution 1917"       : {"name" : "Oktoberrevolution 1917"   , "type":SpecialDayType.INFO_DAY } ,  
    "9. November (Germany)"         : {"name" : "9. November (Deutschland)", "type":SpecialDayType.INFO_DAY } ,  
    "St. Nicholas Day"              : {"name" : "Nikolaus"                 , "type":SpecialDayType.INFO_DAY } ,  
    "Mary Conception"               : {"name" : "Maria Empfängnis"         , "type":SpecialDayType.INFO_DAY } ,  
    "Martin's Day"                  : {"name" : "Martinstag"               , "type":SpecialDayType.INFO_DAY } ,  
    "Winter solstice"               : {"name" : "Wintersonnenwende"        , "type":SpecialDayType.INFO_DAY } ,  
    "Christmas eve"                 : {"name" : "Heiligabend"              , "type":SpecialDayType.INFO_DAY } ,  
    "First christmasday"            : {"name" : "Erster Weihnachtstag"     , "type":SpecialDayType.HOLIDAY  } ,  
    "Second christmasday"           : {"name" : "Zweiter Weihnachtstag"    , "type":SpecialDayType.HOLIDAY  } ,  
    "New Year's Eve"                : {"name" : "Silvester"                , "type":SpecialDayType.INFO_DAY } ,  
} 

class Calender():
    """
    """

class Year:
    def __init__(self, yh, year):
        self.yh   = yh   # year hundred
        self.year = year # year - the last 2 digits
        self.specialDays = dict()
        self.update()

    def __str__(self):
        return f'{self.yh}{self.year}'

    def addSpecialDay(self, specialDay):
        self.specialDays[specialDay._name] = specialDay

    def update(self):
        self.easter = getEaster(self.yh, self.year)
        self.moCw1  = getMoCw1( self.yh, self.year)
        self.ref1 = Day(27, 11, self.yh, self.year) # needed for 1. Advent
        self.ref2 = Day( 1,  5, self.yh, self.year) # needed for Muttertag
        self.ref3 = Day(23, 11, self.yh, self.year) # needed for Buß und Bettag
        self.ref4 = Day( 1, 10, self.yh, self.year) # needed for Erntedank
        self.ref5 = Day( 1,  4, self.yh, self.year) # needed for Sommerzeit
        self.ref6 = Day( 1, 11, self.yh, self.year) # needed for Normalzeit


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

        
        self.addSpecialDay(SpecialDay(name="New Year",                      day= 1, mon= 1, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Holy three kings",              day= 6, mon= 1, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Valentine's day",               day=14, mon= 2, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Women's Day",                   day= 8, mon= 3, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Day of the beer",               day=23, mon= 4, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Labor Day (de)",                day= 1, mon= 5, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Europe day",                    day= 5, mon= 5, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Victory in Europe",             day= 8, mon= 5, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Constitution (de)",             day=23, mon= 5, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Popular uprising DDR 1953",     day=17, mon= 6, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Attack 1944",                   day=20, mon= 7, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Summer solstice",               day=21, mon= 7, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Peace Festival Augsburg",       day= 8, mon= 8, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Assumption Day",                day=15, mon= 8, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Children's Day",                day=20, mon= 9, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Begin WW2 1939",                day= 1, mon=10, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Day of German unity",           day= 3, mon=10, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Hiroshima 1945",                day= 6, mon=10, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Construction of the wall 1961", day=13, mon=10, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Reformation Day 1517",          day=31, mon=10, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="All Saints Day",                day= 1, mon=11, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="All Souls Day",                 day= 2, mon=11, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="October Revolution 1917",       day= 7, mon=11, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="9. November (Germany)",         day= 9, mon=11, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="St. Nicholas Day",              day= 6, mon=12, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Mary Conception",               day= 8, mon=12, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Martin's Day" ,                 day=11, mon=11, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Winter solstice",               day=22, mon=12, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Christmas eve" ,                day=24, mon=12, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="First christmasday",            day=25, mon=12, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="Second christmasday",           day=26, mon=12, yh=self.yh, year=self.year)) 
        self.addSpecialDay(SpecialDay(name="New Year's Eve",                day=31, mon=12, yh=self.yh, year=self.year)) 

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


    def isSpecialDay(self, day, mon):
        retval = list()
        for key, sDay in self.specialDays.items():
            if sDay.day == day and sDay.mon == mon:
                retval.append(sDay)

        return retval

class Day:
    """
    """
    def __init__(self, day, mon, yh, year):
        self.day  = day  # day of the month
        self.mon  = mon  # month of the year
        self.yh   = yh   # year hundred
        self.year = year # year - the last 2 digits

    def __str__(self):
        return f'{WEEK_DAYS_DE.get(self.wd)} - {self.day}.{self.mon}.{self.yh}{self.year}'

    def __eq__(self, other):
        if self.day == other.day and self.mon == other.mon and self.yh == other.yh and self.year == other.year:
            return True
        else:
            return False
            
    def __lt__(self, other):
        if self.yh < other.yh:
            return True
        if self.yh == other.yh and self.year < other.year:
            return True
        if self.yh == other.yh and self.year == other.year and self.mon < other.mon:
            return True
        if self.yh == other.yh and self.year == other.year and self.mon == other.mon and self.day < other.day:
            return True
        return False

    def __gt__(self, other):
        if self.yh > other.yh:
            return True
        if self.yh == other.yh and self.year > other.year:
            return True
        if self.yh == other.yh and self.year == other.year and self.mon > other.mon:
            return True
        if self.yh == other.yh and self.year == other.year and self.mon == other.mon and self.day > other.day:
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
                    if (self.year < 99):
                        self.year += 1
                    else:
                        self.year = 0
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
                    if (self.year > 1):
                        self.year -= 1
                    else:
                        self.year = 99
                        self.yh -= 1                
                self.day = self.daysOfMonth
        return self

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

        aktWoTag = (self.day + int(((mon+1)*26)/10) + year + int(year/4) + int(self.yh/4) - 2*self.yh) % 7
        aktWoTag = aktWoTag + 7 if (aktWoTag < 0) else aktWoTag
        
        return aktWoTag

    @property
    def wd_norm(self):
        wd = self.wd
        wd = wd + 7 if wd < 2 else wd 
        wd -= 2
        return wd

    @property
    def weekday(self):
        return WEEK_DAYS_DE[self.wd]

    @property
    def weekdayShort(self):
        return WEEK_DAYS_DE[self.wd][0:2]
    
    @property
    def cw(self):
        moCw1 = getMoCw1(self.yh, self.year)
        days = self - moCw1
        week = int(days / 7)
        if days < 0:
            weeksOfLastYear = Day(1, 1, self.yh, self.year).decrement(1).cw
            week += weeksOfLastYear
        else:
            week += 1
        return week

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


class SpecialDay(Day):
    def __init__(self, day=1, mon=1, yh=0, year=0, name='', offset=0, incToWeekDay=-1):

        if isinstance(day, Day):
            super(SpecialDay, self).__init__(day.day, day.mon, day.yh, day.year)
        else:
            super(SpecialDay, self).__init__(day, mon, yh, year)
        
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
 
        return f'{WEEK_DAYS_DE.get(self.wd)} - {self.day}.{self.mon}.{self.yh}{self.year} - {self.name} - {dtype}' 

    @property
    def name(self):
        return(TRANSLATE_US_DE[self._name]['name'])

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        return(TRANSLATE_US_DE[self._name]['type'])

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

def getMoCw1(yh, year):
    tmp = Day( 1,  1, yh, year) # needed for Calender week - ISO 8601
    tmp.incToWeekDay(5) # Thursday is always CW 1
    tmp.decrement(3) # now tmp is Monday CW1
    return tmp

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

