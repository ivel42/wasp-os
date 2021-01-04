
# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2021 Andreas Lefevre

"""Calender Configuration for Germany
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from gregorian_calender import SpecialDayType

WEEK_DAYS = {0: 'Montag',
             1: 'Dienstag',
             2: 'Mittwoch',
             3: 'Donnerstag',
             4: 'Freitag',
             5: 'Samstag',
             6: 'Sonntag'}

MONTH_NAMES = {1: 'Januar',
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

NO_SPECIAL_DAY = 'Normaler Tag'

TRANSLATE_DAY = {
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
