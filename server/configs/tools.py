tools = [
    {
        "type": "function",
        "function": {
            "name": "picture_generatin",
            "description": "This is a function used to request thrird party agents/server to generate images based on text provided",  # noqa
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The message from user for image generation",
                    },
                },

            },
            "required": ["message"]
        }
    },

    {
        "type": "function",
        "function": {
            "name": "identifyTask",
            "description": "Identify the task based on user's input",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The message from user for task recognition",
                    },
                    "task": {
                        "type": "string",
                        "enum": ["pictureGeneration", "undefinedTask"],
                        "description": "The supported tasks. AI should choose one task based on user's message.",
                    },
                }
            },
            "required": ["message", "task"]
        }
    }
]
