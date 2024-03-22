"""
Intelligent Dynamic Break Messages for Safe Eyes.
"""

import logging
import requests
import json

# Configuration parameters
use_ollama = False
message_file_path = None

def init(ctx, safeeyes_config, plugin_config):
    """
    Initialize the plugin.
    """

    logging.debug('Initialize Intelligent Dynamic Break Messages plugin')
    global use_ollama, message_file_path, ollama_model, ollama_prompt, ollama_system_prompt
    use_ollama = bool(plugin_config['use_ollama'])
    message_file_path = plugin_config['message_file_path']

    ollama_model = plugin_config['ollama_model']
    ollama_prompt = plugin_config['ollama_prompt']
    ollama_system_prompt = plugin_config['ollama_system_prompt']

def get_ollama_response(model="tinyllama:latest",
                        prompt="Tell me a very short interesting fact.",
                        system_prompt= "You are a helpful assistant.",
                        output_parser=None,
                        max_attempts=10,
                        max_msg_length=400,
                        min_msg_length=20):
    """
    Generate a message using Ollama.
    """
    for attempt in range(max_attempts):
        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post('http://localhost:11434/v1/chat/completions', headers={'Content-Type': 'application/json'}, json=data)
        response_data = response.json()
        if 'choices' in response_data and len(response_data['choices']) > 0:
            message = response_data['choices'][0]['message']['content']

            if output_parser != None:
                processed_message = output_parser(message)
                # Check if the processed message is under the desired character limit
                if len(processed_message) <= max_msg_length and len(processed_message) > min_msg_length:
                    return processed_message
                else:
                    max_msg_length += max_msg_length/20
            else:
                return message
        else:
            return None

        # if 'choices' in response_data and len(response_data['choices']) > 0:
        #     return response_data['choices'][0]['message']['content']
        # return None

def get_widget_title(break_obj):
    """
    Return the widget title.
    """
    return 'Fun Fact!'

def parse_tinyllama_output(message):
    # Split the message by colon and new lines and extract the main fact
    message = message.strip()
    parts = message.split('\n\n', 1)
    if len(parts) >= 1:
        fact_part = parts[0].split(':',1)[1] if ':' in parts[0] else parts[0]
        return fact_part.split('\n')[0].strip()
    return message

def get_widget_content(break_obj):
    """
    Generate or read the break message based on configuration.
    """

    if use_ollama:
        if ollama_model == "tinyllama:latest": # Implement custom parser for tinyllama:latest
            output_parser = parse_tinyllama_output
        else:
            output_parser = None
        output = get_ollama_response(model=ollama_model, prompt=ollama_prompt, system_prompt=ollama_system_prompt, output_parser=output_parser)
        return output or "Enjoy your break!"
    else:
        try:
            with open(message_file_path, 'r') as file:
                return file.read().strip()
        except Exception as e:
            logging.error(f"Error reading break message: {e}")
    return "Enjoy your break!"
