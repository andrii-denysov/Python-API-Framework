DEFAULT_RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "title": {
                "type": "string"
            },
            "author": {
                "type": "string"
            },
            "lines": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "linecount": {
                "type": "string"
            }
        },
        "required": [
            "title",
            "author",
            "lines",
            "linecount"
        ]
    }
}
