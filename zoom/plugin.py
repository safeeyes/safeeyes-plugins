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

"""Zoom plugin skips breaks while in zoom meetings."""

import ast
import logging
import subprocess


context = None


def in_zoom_meeting():
    for name in ['Zoom Meeting', 'as_toolbar']:
        try:
            stdout = subprocess.check_output(
                ['xprop', '-name', name, 'WM_CLASS'], encoding='utf-8')
        except subprocess.CalledProcessError:
            continue
        logging.debug('Found a window named {!r}, {!r}'.format(name, stdout))
        if stdout == 'WM_CLASS(STRING) = "zoom", "zoom"\n':
            logging.debug('In a Zoom meeting')
            return True
    return False


def init(ctx, safeeyes_config, plugin_config):
    global context
    logging.debug('Initialize Zoom plugin')
    context = ctx


def on_pre_break(break_obj):
    return in_zoom_meeting()


def on_start_break(break_obj):
    return in_zoom_meeting()
