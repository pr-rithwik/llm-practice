talker = {
    "type": "function",
    "function": {
        "name": "talker",
        "description": (
            "Give voice to the given message"
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "All the text that needs to be voiced out",
                }
            },
            "required": ["message"],
            "additionalProperties": False,
        },
    },
}