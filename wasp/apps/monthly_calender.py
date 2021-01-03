# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2021 Andreas Lefevre

import wasp
import fonts
import gregorian_calender as greg_cal

class MonthlyCalenderApp():
    """A calender app for wasp-os."""
    NAME = "Monthly Calender"

    def __init__(self):
        now = wasp.watch.rtc.get_localtime()
        self.year = now[0]
        self.mon = now[1]
        self.lut = dict()
        self.lc = [ 0, 24] # lineOffset, lineInc
        self.tc = [10, 29] # tabOffset, tabInc

    def foreground(self):
        self._draw()
        wasp.system.request_event(wasp.EventMask.TOUCH |
                                  wasp.EventMask.SWIPE_UPDOWN)

    def swipe(self, event):
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
        draw = wasp.watch.drawable
        hi =  wasp.system.theme('accent-hi')
        mid = wasp.system.theme('accent-mid')
        lo =  wasp.system.theme('accent-lo')
 
        x = event[1]
        y = event[2]

        found = False

        for d in self.lut:
            ta = self.lut[d][0]
            li = self.lut[d][1]
            if self.tc[0]+self.tc[1]*ta <= x <= self.tc[0]+self.tc[1]*ta+self.tc[1]:
                if self.lc[0]+self.lc[1]*li <= y <= self.lc[0]+self.lc[1]*li+self.lc[1]:
                     found = True
                     break

        draw.fill(x=0, y=190, w=240, h=240-190) 
        if found:
            draw.set_font(fonts.sans17)
            tmp = greg_cal.Year(self.year).isSpecialDay(d, self.mon)
            if len(tmp) == 0:
                draw.set_color(lo)
                draw.string('no special day', 0, 190, width=240)
            else:
                info_line = 0
                for item in tmp:
                    s = item.name
                    if item.type == greg_cal.SpecialDayType.IGNORE:
                        continue
                    if item.type == greg_cal.SpecialDayType.INFO_DAY:
                        draw.set_color(lo)
                    if item.type == greg_cal.SpecialDayType.HOLIDAY:
                        draw.set_color(hi)
                    chunks = draw.wrap(s, 240)
                    for i in range(len(chunks)-1):
                        sub = s[chunks[i]:chunks[i+1]].rstrip()
                        draw.string(sub, 0, 190+self.lc[1]*info_line, width=240)
                        info_line += 1

    def _draw(self):
        draw = wasp.watch.drawable
        hi =  wasp.system.theme('accent-hi')
        mid = wasp.system.theme('accent-mid')
        lo =  wasp.system.theme('accent-lo')

        draw.fill()
        draw.set_color(hi)
        draw.set_font(fonts.sans17)

        line = 0
        tab = 0
 
        y = greg_cal.Year(self.year) 
        s = f'{greg_cal.MONTH_NAMES_DE[self.mon]} {self.year}'
        draw.string(s, self.tc[0]+self.tc[1]*tab, self.lc[0]+self.lc[1]*line, width=240)
        line += 1

        sl = ['KW', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']
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
                    draw.set_color(hi)
                elif d.wd_norm == 6: # So
                    draw.set_color(mid)
                elif dType == greg_cal.SpecialDayType.INFO_DAY: 
                    draw.set_color(mid)
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
