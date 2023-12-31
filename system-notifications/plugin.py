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

"""Diable SafeEyes default notification screen and use system's notifications."""

import logging
import re
import subprocess
import os
import pathlib


context = None
short_break_duration = None
long_break_duration = None



def init(ctx, safeeyes_config, plugin_config):
    global context
    global short_break_duration
    global long_break_duration

    logging.debug('Initialize System Notifications plugin')
    context = ctx
    short_break_duration = safeeyes_config.get('short_break_duration')
    long_break_duration = safeeyes_config.get('long_break_duration')


def on_pre_break(break_obj):
    return False


def on_start_break(break_obj):
    # blocking default notifications and executing a system's default CLI command to run system notifications
    global short_break_duration
    global long_break_duration

    break_type = 'Short break' if break_obj.is_short_break() else 'Long break'

    notification_expire_time = short_break_duration if break_obj.is_short_break() else long_break_duration

    message = break_obj.name
    icon = str(pathlib.Path(__file__).parent.resolve()) + '/system-notification-icon.png'

    subprocess.Popen([
    'notify-send',
    	'--expire-time', str(notification_expire_time*1000), # miliseconds are expected
    	'--icon', icon,
    	'--urgency', 'low',
    	'--hint' , 'int:transient:1', # don't save in notification history
    	break_type,
    	message
    ])

    return True
