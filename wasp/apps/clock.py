# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2020 Daniel Thompson

"""Digital clock
~~~~~~~~~~~~~~~~

Shows a time (as HH:MM) together with a battery meter and the date.
"""

import wasp

#from wasp import watch.drawable as draw

import icons
import fonts
import fonts.clock as digits
import gregorian_calender as greg_cal


DIGITS = (
        digits.clock_0, digits.clock_1, digits.clock_2, digits.clock_3,
        digits.clock_4, digits.clock_5, digits.clock_6, digits.clock_7,
        digits.clock_8, digits.clock_9
)

class ClockApp():
    """Simple digital clock application.

    .. figure:: res/ClockApp.png
        :width: 179

        Screenshot of the clock application
    """
    NAME = 'Clock'
    ICON = icons.clock

    def __init__(self):
        self._min = -1
        self._day = -1
        self._year = -1

        # init the calender
        now = wasp.watch.rtc.get_localtime()
        self.year = greg_cal.Year(now[0])
        self.calDay = greg_cal.Day(now[2], now[1], now[0])

        self.dDayIdx = 0
        self._tickDivider = 2
        self._tick = 0

    def foreground(self):
        """Activate the application.

        Configure the status bar, redraw the display and request a periodic
        tick callback every second.
        """
        wasp.system.bar.clock = False
        self._draw(True)
        wasp.system.request_tick(1000)
 
    def sleep(self):
        """Prepare to enter the low power mode.

        :returns: True, which tells the system manager not to automatically
                  switch to the default application before sleeping.
        """
        return True

    def wake(self):
        """Return from low power mode.

        Time will have changes whilst we have been asleep so we must
        udpate the display (but there is no need for a full redraw because
        the display RAM is preserved during a sleep.
        """
        self._draw()

    def tick(self, ticks):
        """Periodic callback to update the display."""
        self._tick += 1
        if self._tick >= self._tickDivider:
            self._tick = 0
            self.dDayIdx += 1
            self._updateDisplayDay()

        self._draw()
 
    def _clear(self):
        draw = wasp.watch.drawable
        hi =  wasp.system.theme('accent-hi')
        mid = wasp.system.theme('accent-mid')
        lo =  wasp.system.theme('accent-lo')

        # Clear the display and draw that static parts of the watch face
        draw.fill()
        draw.blit(digits.clock_colon, 2*48, 80, fg=mid)

        # Redraw the status bar
        wasp.system.bar.draw()

    def _draw(self, redraw=False):
        """Draw or lazily update the display.

        The updates are as lazy by default and avoid spending time redrawing
        if the time on display has not changed. However if redraw is set to
        True then a full redraw is be performed.
        """

        # The update is doubly lazy... we update the status bar and if
        # the status bus update reports a change in the time of day 
        # then we compare the minute on display to make sure we 
        # only update the main clock once per minute.
        now = wasp.system.bar.update()
        
        if now and (redraw or (self._day != now[2])):
            # Record the day that is currently being displayed
            self._clear()
            self._drawPerDay(now)
            redraw = True

        if now and (redraw or (self._min != now[4])):
            # Record the minute that is currently being displayed
            self._min = now[4]
            self._drawPerMin(now)

    def _drawPerDay(self, now):
        draw = wasp.watch.drawable
        hi =  wasp.system.theme('accent-hi')
        mid = wasp.system.theme('accent-mid')
        lo =  wasp.system.theme('accent-lo')

        # update calender
        if self._day == now[2]:
            pass
        elif self._day + 1 == now[2]:
            self.calDay.increment(1)
        else:
            # complied reinit - should not happen
            self.calDay = greg_cal.Day(now[2], now[1], now[0])
        self._day = now[2]

        if self._year != now[0]:
            self.year = greg_cal.Year(now[0])
            self._year = now[0]

        # draw current date
        d = self.calDay
        draw.set_color(mid)
        draw.set_font(fonts.sans24)
        draw.string('{} {} {}.{}.{}'.format(d.cw, d.weekdayShort, d.day, d.mon, d.year),
                0, 160, width=240)
        
        # draw date info
        self._updateDisplayDay()

    def _updateDisplayDay(self):
        draw = wasp.watch.drawable
        hi =  wasp.system.theme('accent-hi')
        mid = wasp.system.theme('accent-mid')
        lo =  wasp.system.theme('accent-lo')
        d = self.calDay

        draw.fill(x=0, y=190, w=240, h=240-190) 
        draw.set_font(fonts.sansMono18)
        tmp = self.year.isSpecialDay(d.day, d.mon)
        if len(tmp) < 2:
            self._tickDivider = 60
        else:
            self._tickDivider = 2
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
                draw.string(sub, 0, 190+24*info_line, width=240)
                info_line += 1

    def _drawPerMin(self, now):
 
        draw = wasp.watch.drawable
        hi =  wasp.system.theme('accent-hi')
        mid = wasp.system.theme('accent-mid')
        lo =  wasp.system.theme('accent-lo')
 
        # Draw the changeable parts of the watch face
        draw.blit(DIGITS[now[4]  % 10], 4*48, 80, fg=hi)
        draw.blit(DIGITS[now[4] // 10], 3*48, 80, fg=lo)
        draw.blit(DIGITS[now[3]  % 10], 1*48, 80, fg=hi)
        draw.blit(DIGITS[now[3] // 10], 0*48, 80, fg=lo)
