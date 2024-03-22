# Intelligent Dynamic Break Messages

This Safe Eyes plugin displays dynamic break messages during breaks. It reads a file and shows the string in it.
## Installation

2. Install the plugin into Safe Eyes by placing it in `~/.config/safeeyes/plugins/dynamic_break_messages`.
3. Configure the plugin through Safe Eyes settings. Add this part to safeeyes config `~/.config/safeeyes/safeeyes.json`:

```
    "plugins": [

        ...

        {
            "enabled": true,
            "id": "dynamic_break_messages",
            "settings": {
                "message_file_path": "/tmp/safeeyes_message.txt"
            },
            "version": "0.1"
        },
    ]
```

## Configuration

- `message_file_path`: Specify the file path to read break message from.
