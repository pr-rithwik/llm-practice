artist = {
    "type": "function",
    "function": {
        "name": "artist",
        "description": (
            "Generate an image for the given city in pop style"
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city to which an image is needed ",
                }
            },
            "required": ["city"],
            "additionalProperties": False,
        },
    },
}