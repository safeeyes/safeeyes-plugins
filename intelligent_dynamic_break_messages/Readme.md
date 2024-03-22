# Intelligent Dynamic Break Messages

This Safe Eyes plugin displays dynamic break messages during breaks. It is complicated version of Dynamic Break Message plugin. It can generate messages dynamically using [Ollama(Local LLM runner)](http://ollama.ai/) or read them from a specified file.

## Installation

1. Ensure Ollama is installed and a model is dowloaded(e.g. Install tinyllama with command `ollama run tinyllama:latest` or find other models like mistral in [ollama library](https://ollama.com/library)).
2. Install the plugin into Safe Eyes by placing it in `~/.config/safeeyes/plugins/intelligent_dynamic_break_messages`.
3. Configure the plugin through Safe Eyes settings. Add this part to safeeyes config `~/.config/safeeyes/safeeyes.json`:

```
    "plugins": [

        ...

        {
            "enabled": true,
            "id": "intelligent_dynamic_break_messages",
            "settings": {
                "message_file_path": "/tmp/safeeyes_message.txt",
                "ollama_model": "dolphin-mistral:v2.1",
                "ollama_prompt": "Tell me a very short interesting fact.",
                "ollama_system_prompt": "You are a helpful assistant.",
                "use_ollama": "true"
            },
            "version": "0.1"
        }
    ]
```

## Configuration

- `use_ollama`: Toggle this to `true` to use Ollama for generating messages. Otherwise, messages will be read from the specified file.
- `ollama_model`: Ollama model (default is **tinyllama:latest**)
- `ollama_prompt`: LLM prompt.
- `ollama_system_prompt`: LLM system prompt
- `message_file_path`: Specify the file path to read break messages from when not using Ollama.

If any of the above variable set incorrectly, Plugin just shows "Enjoy your break!".

## Dependencies

- Ollama command.

Enjoy more personalized and intelligent break messages with Safe Eyes!