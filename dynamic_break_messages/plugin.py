"""
Display dynamic messages during breaks.
"""

import logging

message_file_path = None
break_message = None

def init(ctx, safeeyes_config, plugin_config):
    """
    Initialize the plugin.
    """
    logging.debug('Initialize Dynamic Break Messages plugin')
    global message_file_path
    message_file_path = plugin_config['message_file_path']

def get_widget_title(break_obj):
    """
    Return the widget title. This could be a fixed title or based on the message content.
    """
    return 'Message:'

def get_widget_content(break_obj):
    """
    Return the dynamic break message.
    """
    global break_message
    try:
        with open(message_file_path, 'r') as file:
            break_message = file.read().strip()
    except Exception as e:
        logging.error(f"Error reading break message: {e}")
        break_message = None
    return break_message
