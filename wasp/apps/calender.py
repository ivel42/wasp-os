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

class SpecialDayType():
    INFO_DAY = 1
    HOLIDAY  = 2


TRANSLATE_US_DE = {
    "Women's Shrovetide"            : "Weiberfastnacht"           ,                               
    "Carnival Monday"               : "Rosenmontag"               ,           
    "Shrove Tuesday"                : "Faschingsdienstag"         ,                 
    "Ash Wednesday"                 : "Aschermittwoch"            ,              
    "Palm Sunday"                   : "Palmsonntag"               ,           
    "Maundy Thursday"               : "Gründonnerstag"            ,              
    "Good Friday"                   : "Karfreitag"                ,          
    "Holy Saturday"                 : "Karsamstag"                ,          
    "Easter Sunday"                 : "Oster-Sonntag"             ,             
    "Easter Monday"                 : "Oster-Montag"              ,            
    "White Sunday"                  : "Weißer Sonntag"            ,              
    "Fathers day"                   : "Vatertag"                  ,        
    "Ascension of Christ"           : "Christi Himmelfahrt"       ,                   
    "Pentecost Sunday"              : "Pfingstsonntag"            ,              
    "Whit Monday"                   : "Pfingstmontag"             ,             
    "Corpus Christi"                : "Fronleichnam"              ,            
    "Memorial Day (de)"             : "Volkstrauertag (de)"       ,                   
    "1 Advent"                      : "1. Advent"                 ,         
    "2 Advent"                      : "2. Advent"                 ,         
    "3 Advent"                      : "3. Advent"                 ,         
    "4 Advent"                      : "4. Advent"                 ,         
    "Mother's Day"                  : "Muttertag"                 ,         
    "Thanksgiving (de)"             : "Erntedank"                 ,         
    "Buß- und Bettag"               : "Buß- und Bettag"           ,               
    "Summertime (eu)"               : "Sommerzeit"                ,          
    "Normaltime (eu)"               : "Normalzeit"                ,          
    "New Year"                      : "Neujahr"                   ,       
    "Holy three kings"              : "Hl. Drei Könige"           ,               
    "Valentine's day"               : "Valentinstag"              ,            
    "Day of the beer"               : "Tag des Bieres"            ,              
    "Labor Day (de)"                : "Tag der Arbeit (de)"       ,                   
    "Europe day"                    : "Europatag"                 ,         
    "Victory in Europe"             : "Kriegsende 2. WK 1945"     ,                     
    "Constitution (de)"             : "Grundgesetz (de)"          ,                
    "Popular uprising DDR 1953"     : "Volksaufstand DDR 1953"    ,                      
    "Attack 1944"                   : "Attentat 1944"             ,             
    "Summer solstice"               : "Sommersonnenwende"         ,                 
    "Assumption Day"                : "Mariä Himmelfahrt"         ,                 
    "Begin WW2 1939"                : "Kriegsbeginn 2. WK 1939"   ,                       
    "Day of German unity"           : "Tag der Deutschen Einheit" ,                         
    "Hiroshima 1945"                : "Hiroshima 1945"            ,              
    "Construction of the wall 1961" : "Mauerbau 1961"             ,             
    "Reformation Day 1517"          : "Reformationstag 1517"      ,                    
    "All Saints Day"                : "Allerheiligen"             ,             
    "All Souls Day"                 : "Allerseelen"               ,             
    "October Revolution 1917"       : "Oktoberrevolution 1917"    ,                      
    "9. November (Germany)"         : "9. November (Deutschland)" ,                         
    "St. Nicholas Day"              : "Nikolaus"                  ,        
    "Mary Conception"               : "Maria Empfängnis"          ,                
    "Martin's Day"                  : "Martinstag"                ,          
    "Winter solstice"               : "Wintersonnenwende"         ,                 
    "Christmas eve"                 : "Heiligabend"               ,           
    "First christmasday"            : "Erster Weihnachtstag"      ,                    
    "Second christmasday"           : "Zweiter Weihnachtstag"     ,                     
    "New Year's Eve"                : "Silvester"                 ,                           
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

    def addSpecialDay(self, specialDay):
        self.specialDays[specialDay.name] = specialDay

    def update(self):
        self.easter = getEaster(self.yh, self.year)
        self.ref1 = Day(27, 11, self.yh, self.year) # needed for 1. Advent
        self.ref2 = Day( 1,  5, self.yh, self.year) # needed for Muttertag
        self.ref3 = Day(23, 11, self.yh, self.year) # needed for Buß und Bettag
        self.ref4 = Day( 1, 10, self.yh, self.year) # needed for Erntedank
        self.ref5 = Day( 1,  4, self.yh, self.year) # needed for Sommerzeit
        self.ref6 = Day( 1, 11, self.yh, self.year) # needed for Normalzeit

        self.addSpecialDay(SpecialDay(name="Women's Shrovetide",   day=self.easter, offset= -52)) # Infotage - donnertag vor aschermittwoch
        self.addSpecialDay(SpecialDay(name="Carnival Monday",      day=self.easter, offset= -48)) # Infotage
        self.addSpecialDay(SpecialDay(name="Shrove Tuesday",       day=self.easter, offset= -47)) # Infotage
        self.addSpecialDay(SpecialDay(name="Ash Wednesday",        day=self.easter, offset= -46)) # Infotage
        self.addSpecialDay(SpecialDay(name="Palm Sunday",          day=self.easter, offset=  -7)) # Infotage - Sonntag vor Ostern
        self.addSpecialDay(SpecialDay(name="Maundy Thursday",      day=self.easter, offset=  -3)) # Infotage
        self.addSpecialDay(SpecialDay(name="Good Friday",          day=self.easter, offset=  -2)) # Feiertage
        self.addSpecialDay(SpecialDay(name="Holy Saturday",        day=self.easter, offset=  -1)) # Infotage
        self.addSpecialDay(SpecialDay(name="Easter Sunday",        day=self.easter))              # Infotage
        self.addSpecialDay(SpecialDay(name="Easter Monday",        day=self.easter, offset=   1)) # Feiertage
        self.addSpecialDay(SpecialDay(name="White Sunday"  ,       day=self.easter, offset=   7)) # Infotage
        self.addSpecialDay(SpecialDay(name="Fathers day" ,         day=self.easter, offset=  39)) # Infotage
        self.addSpecialDay(SpecialDay(name="Ascension of Christ" , day=self.easter, offset=  39)) # Feiertage
        self.addSpecialDay(SpecialDay(name="Pentecost Sunday" ,    day=self.easter, offset=  49)) # Infotage
        self.addSpecialDay(SpecialDay(name="Whit Monday",          day=self.easter, offset=  50)) # Feiertage
        self.addSpecialDay(SpecialDay(name="Corpus Christi" ,      day=self.easter, offset=  60)) # Feiertage

        self.addSpecialDay(SpecialDay(name="Memorial Day (de)", day=self.ref1, offset=-14, incToWeekDay=1)) # Infotage - am zweiten Sonntag vor dem 1. Adventssonntag
        self.addSpecialDay(SpecialDay(name="1 Advent",          day=self.ref1, incToWeekDay=1))            # Infotage - liegt zwischen dem 27. November und dem 3. Dezember
        self.addSpecialDay(SpecialDay(name="2 Advent",          day=self.ref1, offset=7, incToWeekDay=1))  # Infotage
        self.addSpecialDay(SpecialDay(name="3 Advent",          day=self.ref1, offset=14, incToWeekDay=1)) # Infotage
        self.addSpecialDay(SpecialDay(name="4 Advent",          day=self.ref1, offset=21, incToWeekDay=1)) # Infotage

        self.addSpecialDay(SpecialDay(name="Mother's Day",      day=self.ref2, offset=7, incToWeekDay=1)) # Infotage zweiten Sonntag im Mai statt
        
        self.addSpecialDay(SpecialDay(name="Thanksgiving (de)", day=self.ref4, incToWeekDay=1)) # Infotage

        self.addSpecialDay(SpecialDay(name="Buß- und Bettag",   day=self.ref3, offset=7, incToWeekDay=4)) # Infotage Mittwoch vor dem 23. November
        
        self.addSpecialDay(SpecialDay(name="Summertime (eu)",   day=self.ref5, offset= -7, incToWeekDay=1)) # Infotage letzter sonntag im märz
        self.addSpecialDay(SpecialDay(name="Normaltime (eu)",   day=self.ref6, offset= -7, incToWeekDay=1)) # Infotage letzter sonntag im oktober

        
        self.addSpecialDay(SpecialDay(name="New Year",                      day= 1, mon= 1, yh=self.yh, year=self.year)) # Feiertage
        self.addSpecialDay(SpecialDay(name="Holy three kings",              day= 6, mon= 1, yh=self.yh, year=self.year)) # Feiertage
        self.addSpecialDay(SpecialDay(name="Valentine's day",               day=14, mon= 2, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Day of the beer",               day=23, mon= 4, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Labor Day (de)",                day= 1, mon= 5, yh=self.yh, year=self.year)) # Feiertage
        self.addSpecialDay(SpecialDay(name="Europe day",                    day= 5, mon= 5, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Victory in Europe",             day= 8, mon= 5, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Constitution (de)",             day=23, mon= 5, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Popular uprising DDR 1953",     day=17, mon= 6, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Attack 1944",                   day=20, mon= 7, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Summer solstice",               day=21, mon= 7, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Assumption Day",                day=15, mon= 8, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Begin WW2 1939",                day= 1, mon=10, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Day of German unity",           day= 3, mon=10, yh=self.yh, year=self.year)) # Feiertage
        self.addSpecialDay(SpecialDay(name="Hiroshima 1945",                day= 6, mon=10, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Construction of the wall 1961", day=13, mon=10, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Reformation Day 1517",          day=31, mon=10, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="All Saints Day",                day= 1, mon=11, yh=self.yh, year=self.year)) # Feiertage
        self.addSpecialDay(SpecialDay(name="All Souls Day" ,                day= 2, mon=11, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="October Revolution 1917",       day= 7, mon=11, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="9. November (Germany)" ,        day= 9, mon=11, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="St. Nicholas Day",              day= 6, mon=12, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Mary Conception",               day= 8, mon=12, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Martin's Day" ,                 day=11, mon=11, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="Winter solstice",               day=22, mon=12, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name= "Christmas eve" ,               day=24, mon=12, yh=self.yh, year=self.year)) # Infotage
        self.addSpecialDay(SpecialDay(name="First christmasday",            day=25, mon=12, yh=self.yh, year=self.year)) # Feiertage
        self.addSpecialDay(SpecialDay(name="Second christmasday",           day=26, mon=12, yh=self.yh, year=self.year)) # Feiertage
        self.addSpecialDay(SpecialDay(name= "New Year's Eve",               day=31, mon=12, yh=self.yh, year=self.year)) # Infotage

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

