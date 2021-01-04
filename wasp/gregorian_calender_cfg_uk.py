
# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2021 Andreas Lefevre

"""Calender Configuration for UK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from gregorian_calender import SpecialDayType

WEEK_DAYS = {0: 'Monday',
             1: 'Tuesday',
             2: 'Wednesday',
             3: 'Thursday',
             4: 'Friday',
             5: 'Saturday',
             6: 'Sunday'}

MONTH_NAMES = {1: 'January',
               2: 'February',
               3: 'March',
               4: 'April',
               5: 'May',
               6: 'June',
               7: 'July',
               8: 'August',
               9: 'September',
              10: 'October',
              11: 'November',
              12: 'December'}

NO_SPECIAL_DAY = 'normal day'

TRANSLATE_DAY = {
    "Women's Shrovetide"            : {"name" : "Women's Shrovetide"            , "type":SpecialDayType.INFO_DAY } ,       
    "Carnival Monday"               : {"name" : "Carnival Monday"               , "type":SpecialDayType.INFO_DAY } , 
    "Shrove Tuesday"                : {"name" : "Shrove Tuesday"                , "type":SpecialDayType.INFO_DAY } , 
    "Ash Wednesday"                 : {"name" : "Ash Wednesday"                 , "type":SpecialDayType.INFO_DAY } , 
    "Palm Sunday"                   : {"name" : "Palm Sunday"                   , "type":SpecialDayType.INFO_DAY } , 
    "Maundy Thursday"               : {"name" : "Maundy Thursday"               , "type":SpecialDayType.INFO_DAY } , 
    "Good Friday"                   : {"name" : "Good Friday"                   , "type":SpecialDayType.HOLIDAY  } , 
    "Holy Saturday"                 : {"name" : "Holy Saturday"                 , "type":SpecialDayType.INFO_DAY } , 
    "Easter Sunday"                 : {"name" : "Easter Sunday"                 , "type":SpecialDayType.INFO_DAY } , 
    "Easter Monday"                 : {"name" : "Easter Monday"                 , "type":SpecialDayType.HOLIDAY  } , 
    "White Sunday"                  : {"name" : "White Sunday"                  , "type":SpecialDayType.INFO_DAY } , 
    "Fathers day"                   : {"name" : "Fathers day"                   , "type":SpecialDayType.INFO_DAY } , 
    "Ascension of Christ"           : {"name" : "Ascension of Christ"           , "type":SpecialDayType.INFO_DAY } , 
    "Pentecost Sunday"              : {"name" : "Pentecost Sunday"              , "type":SpecialDayType.INFO_DAY } , 
    "Whit Monday"                   : {"name" : "Whit Monday"                   , "type":SpecialDayType.INFO_DAY } , 
    "Corpus Christi"                : {"name" : "Corpus Christi"                , "type":SpecialDayType.INFO_DAY } , 
    "Memorial Day (de)"             : {"name" : "Memorial Day (de)"             , "type":SpecialDayType.IGNORE   } ,           
    "1 Advent"                      : {"name" : "1 Advent"                      , "type":SpecialDayType.INFO_DAY } ,        
    "2 Advent"                      : {"name" : "2 Advent"                      , "type":SpecialDayType.INFO_DAY } , 
    "3 Advent"                      : {"name" : "3 Advent"                      , "type":SpecialDayType.INFO_DAY } , 
    "4 Advent"                      : {"name" : "4 Advent"                      , "type":SpecialDayType.INFO_DAY } , 
    "Mother's Day"                  : {"name" : "Mother's Day"                  , "type":SpecialDayType.INFO_DAY } , 
    "Thanksgiving (de)"             : {"name" : "Harvest festival (de)"         , "type":SpecialDayType.INFO_DAY } , 
    "Buß- und Bettag"               : {"name" : "Buß- und Bettag"               , "type":SpecialDayType.INFO_DAY } , 
    "Summertime (eu)"               : {"name" : "Summertime (eu)"               , "type":SpecialDayType.INFO_DAY } ,  
    "Normaltime (eu)"               : {"name" : "Normaltime (eu)"               , "type":SpecialDayType.INFO_DAY } ,    
    "New Year"                      : {"name" : "New Year"                      , "type":SpecialDayType.HOLIDAY  } ,  
    "Holy three kings"              : {"name" : "Holy three kings"              , "type":SpecialDayType.INFO_DAY } ,  
    "Valentine's day"               : {"name" : "Valentine's day"               , "type":SpecialDayType.INFO_DAY } ,  
    "Women's Day"                   : {"name" : "Women's Day"                   , "type":SpecialDayType.INFO_DAY } ,  
    "Day of the beer"               : {"name" : "Day of the beer"               , "type":SpecialDayType.INFO_DAY } ,  
    "Labor Day (de)"                : {"name" : "Labor Day (de)"                , "type":SpecialDayType.IGNORE   } ,  
    "Europe day"                    : {"name" : "Europe day"                    , "type":SpecialDayType.INFO_DAY } ,  
    "Victory in Europe"             : {"name" : "Victory in Europe"             , "type":SpecialDayType.INFO_DAY } ,  
    "Constitution (de)"             : {"name" : "Constitution (de)"             , "type":SpecialDayType.IGNORE   } ,  
    "Popular uprising DDR 1953"     : {"name" : "Popular uprising DDR 1953"     , "type":SpecialDayType.IGNORE   } ,  
    "Attack 1944"                   : {"name" : "Attack 1944"                   , "type":SpecialDayType.IGNORE   } ,  
    "Summer solstice"               : {"name" : "Summer solstice"               , "type":SpecialDayType.INFO_DAY } ,  
    "Peace Festival Augsburg"       : {"name" : "Peace Festival Augsburg"       , "type":SpecialDayType.IGNORE   } ,  
    "Assumption Day"                : {"name" : "Assumption Day"                , "type":SpecialDayType.INFO_DAY } ,  
    "Children's Day"                : {"name" : "Children's Day"                , "type":SpecialDayType.INFO_DAY } ,  
    "Begin WW2 1939"                : {"name" : "Begin WW2 1939"                , "type":SpecialDayType.IGNORE   } ,  
    "Day of German unity"           : {"name" : "Day of German unity"           , "type":SpecialDayType.IGNORE   } ,  
    "Hiroshima 1945"                : {"name" : "Hiroshima 1945"                , "type":SpecialDayType.IGNORE   } ,  
    "Construction of the wall 1961" : {"name" : "Construction of the wall 1961" , "type":SpecialDayType.IGNORE   } ,  
    "Reformation Day 1517"          : {"name" : "Reformation Day 1517"          , "type":SpecialDayType.IGNORE   } ,  
    "All Saints Day"                : {"name" : "All Saints Day"                , "type":SpecialDayType.INFO_DAY } ,  
    "All Souls Day"                 : {"name" : "All Souls Day"                 , "type":SpecialDayType.INFO_DAY } ,  
    "October Revolution 1917"       : {"name" : "October Revolution 1917"       , "type":SpecialDayType.INFO_DAY } ,  
    "9. November (Germany)"         : {"name" : "9. November (Germany)"         , "type":SpecialDayType.IGNORE   } ,  
    "St. Nicholas Day"              : {"name" : "St. Nicholas Day"              , "type":SpecialDayType.INFO_DAY } ,  
    "Mary Conception"               : {"name" : "Mary Conception"               , "type":SpecialDayType.INFO_DAY } ,  
    "Martin's Day"                  : {"name" : "Martin's Day"                  , "type":SpecialDayType.INFO_DAY } ,  
    "Winter solstice"               : {"name" : "Winter solstice"               , "type":SpecialDayType.INFO_DAY } ,  
    "Christmas eve"                 : {"name" : "Christmas eve"                 , "type":SpecialDayType.INFO_DAY } ,  
    "First christmasday"            : {"name" : "Christmas Day"                 , "type":SpecialDayType.HOLIDAY  } ,  
    "Second christmasday"           : {"name" : "Second christmasday"           , "type":SpecialDayType.INFO_DAY } ,  
    "New Year's Eve"                : {"name" : "New Year's Eve"                , "type":SpecialDayType.INFO_DAY } ,  
} 
