#!/usr/bin/env python
# Safe Eyes is a utility to remind you to take break frequently
# to protect your eyes from eye strain.

# Copyright (C) 2017  Gobinath

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Show the current weather on break screen.
"""

import logging
import pyowm

api = None
location = None
owm = None
weather_details = None

def init(ctx, safeeyes_config, plugin_config):
    """
    Initialize the plugin.
    """
    logging.debug('Initialize Weather plugin')
    global api
    global location
    global owm
    api = plugin_config['api']
    location = plugin_config['location']
    if api != "" and location != "":
        owm = pyowm.OWM(api)
    

def get_widget_title(break_obj):
    """
    Return the widget title.
    """
    logging.debug('Get the weather information')
    global weather_details
    if owm:
        try:
            observation = owm.weather_at_place(location)
            weather = observation.get_weather()
            temp = weather.get_temperature('celsius').get('temp')
            humidity = weather.get_humidity()
            wind_speed = weather.get_wind().get('speed')
            weather_details = 'Temperature: %s℃\t\tHumidity: %s\tWind Speed: %s' % (temp, humidity, wind_speed)
        except BaseException:
            # Can be a network error
            weather_details = None
    if weather_details:
        return 'Weather'

def get_widget_content(break_obj):
    """
    Return the weather details.
    """
    return weather_details
