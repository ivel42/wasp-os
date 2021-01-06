# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2021 Andreas Lefevre

"""Monthly calender
~~~~~~~~~~~~~~~~~~~

An application to show an Perpetual Calendar.

    .. figure:: res/MonthlyCalenderApp.png
        :width: 179

        Screenshot of the Calender Application

**Display Sections**

*Selected Month*:
    The first line shows the displayed month and year.

*Calender*:
    Displays the selected month. The color encodes the 
    type of the day. See gregorian_calender.py dayColors.

*Special Day Info*:
    The next lines show the name of the selected special day.

**Controls**

Touch on a day in the *Calender*: 
    Select that date for the *Special Day Info*.

Swipe up/down: 
    Change the displayed month on the *Calender*.

"""

import wasp
import fonts
import gregorian_calender as greg_cal

class MonthlyCalenderApp():
    """A perpetual calender app for wasp-os.
    """

    NAME = "Monthly Calender"

    def __init__(self):
        """ Initialize instance variables
        """

        # get the current time time to use it
        # as starting point
        now = wasp.watch.rtc.get_localtime()
        self.year = now[0]
        self.mon = now[1]
        self.dDay = now[2]

        # index of the *Special Day Info* 
        # needed if there is more than one special day per day
        self.dDayIdx = 0

        # look up table to remember line and colum of each day
        self.lut = dict()

        # line and column definition
        self.lc = [ 0, 24] # lineOffset, lineInc
        self.tc = [10, 29] # tabOffset, tabInc

    def foreground(self):
        """Activate the application.
        
        - Request touch and swipe
        - Draw everything
        """
        self._draw()
        wasp.system.request_event(wasp.EventMask.TOUCH |
                                  wasp.EventMask.SWIPE_UPDOWN)
    def tick(self, ticks):
        """Periodic callback.
        
        - Draw *Special Day Info*
        """
        self.dDayIdx += 1
        self._updateDisplayDay()

    def swipe(self, event):
        """Swipe callback.
        
        up:
            Increment month to be displayed
        down:
            Increment month to be displayed

        - Draw everything
        """
        if event[0] == wasp.EventType.UP:
            if self.mon < 12:
                self.mon += 1
            else:
                self.mon = 1
                self.year += 1
        else:
            if self.mon > 1:
                self.mon -= 1
            else:
                self.mon = 12
                self.year -= 1
        self._draw()

    def touch(self, event):
        """Touch callback.
        
        - Find the day that was touched
        - Draw *Special Day Info*
        """
        x = event[1]
        y = event[2]

        for d in self.lut:
            ta = self.lut[d][0]
            li = self.lut[d][1]
            if self.tc[0]+self.tc[1]*ta <= x <= self.tc[0]+self.tc[1]*ta+self.tc[1]:
                if self.lc[0]+self.lc[1]*li <= y <= self.lc[0]+self.lc[1]*li+self.lc[1]:
                     self.dDay = d
                     break
        
        self._updateDisplayDay()

    def _updateDisplayDay(self):
        """Draw *Special Day Info*
        
        - Clear this part of the display
        - Get a list of the special days
        - Request faster tick to toggle special days when there is more than one
        - Draw the name of the day in the right color
        """
        draw = wasp.watch.drawable
        hi =  wasp.system.theme('bright')
        lo =  wasp.system.theme('mid')
        mid = draw.lighten(lo, 1)

        draw.fill(x=0, y=190, w=240, h=240-190) 
        draw.set_font(fonts.sansMono18)
        tmp = greg_cal.Year(self.year).specialDayList(self.dDay, self.mon)
        if len(tmp) < 2:
            wasp.system.request_tick(60000)
        else:
            wasp.system.request_tick(2000)
        if len(tmp) == 0:
            draw.set_color(lo)
            draw.string(greg_cal.cfg.NO_SPECIAL_DAY, 0, 190, width=240)
        else:
            dIdx = self.dDayIdx = self.dDayIdx % len(tmp)
            info_line = 0
            item = tmp[dIdx]
            s = item.name
            if item.type == greg_cal.SpecialDayType.IGNORE:
                draw.set_color(lo)
            if item.type == greg_cal.SpecialDayType.INFO_DAY:
                draw.set_color(greg_cal.dayColors['infoday'])
            if item.type == greg_cal.SpecialDayType.HOLIDAY:
                draw.set_color(greg_cal.dayColors['holiday'])
            chunks = draw.wrap(s, 240)
            for i in range(len(chunks)-1):
                sub = s[chunks[i]:chunks[i+1]].rstrip()
                draw.string(sub, 0, 190+self.lc[1]*info_line, width=240)
                info_line += 1

    def _draw(self):
        """Draw everything
        
        - Clear the display
        - Draw *Selected Month*
        - Draw *Calender*
        - Draw *Special Day Info*
        """
        draw = wasp.watch.drawable
        hi =  wasp.system.theme('bright')
        lo =  wasp.system.theme('mid')
        mid = draw.lighten(lo, 1)

        draw.fill()
        draw.set_color(hi)
        draw.set_font(fonts.sansMono18)

        line = 0
        tab = 0
 
        y = greg_cal.Year(self.year) 
        s = f'{greg_cal.cfg.MONTH_NAMES[self.mon]} {self.year}'
        draw.string(s, self.tc[0]+self.tc[1]*tab, self.lc[0]+self.lc[1]*line, width=240)
        line += 1

        sl = ['CW']
        for wd in greg_cal.cfg.WEEK_DAYS:
            sl.append(greg_cal.cfg.WEEK_DAYS[wd][0:2])
        for s in sl:
            draw.string(s, self.tc[0]+self.tc[1]*tab, self.lc[0]+self.lc[1]*line)
            tab += 1
        line += 1
        tab = 0
        
        self.lut.clear()
        d = greg_cal.Day(1, self.mon, self.year)
        while d.mon == self.mon:
            draw.set_color(hi)
            draw.string(f'{d.cw}', self.tc[0]+self.tc[1]*tab, self.lc[0]+self.lc[1]*line)
            tab += 1
            tab += d.wd_norm
            while d.mon == self.mon:
                dType = y.specialDayType(d.day, d.mon)
                if dType == greg_cal.SpecialDayType.HOLIDAY: 
                    draw.set_color(greg_cal.dayColors['holiday'])
                elif dType == greg_cal.SpecialDayType.INFO_DAY: 
                    draw.set_color(greg_cal.dayColors['infoday'])
                elif d.wd_norm == 6: # So
                    draw.set_color(greg_cal.dayColors['sunday'])
                else:
                    draw.set_color(lo)
                draw.string(f'{d.day}', self.tc[0]+self.tc[1]*tab, self.lc[0]+self.lc[1]*line, width=self.tc[1])
                self.lut.update({d.day:(tab, line)})
                tab += 1
                d.increment(1)
                if d.wd_norm == 0:
                    line += 1
                    tab = 0
                    break
        
        self._updateDisplayDay()