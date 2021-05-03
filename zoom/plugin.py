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
    try:
        # Attempt to change the order of on_pre_break plugins so that
        # the zoom plugin occurs before the notification plugin to avoid
        # seeing break notifications while in Zoom meetings.
        # The SafeEyes and PluginManager class instances are not
        # provided to plugins in any form except through non-public
        # references attached to closures provided by api references.
        # This works in CPython, but it is a hack, so any errors that
        # might occur are logged and ignored.
        safeeyes = ctx['api']['show_about'].__closure__[0].cell_contents
        on_pre_break = safeeyes.plugins_manager._PluginManager__plugins_on_pre_break
        for i, plugin in enumerate(on_pre_break):
            if plugin['id'] == 'zoom':
                on_pre_break.insert(0, on_pre_break.pop(i))
                break
        logging.debug('on_pre_break plugin order: %r', [i['id'] for i in on_pre_break])
    except Exception:
        logging.exception('Error updating the order of on_pre_break plugins')


def on_pre_break(break_obj):
    return in_zoom_meeting()


def on_start_break(break_obj):
    return in_zoom_meeting()
