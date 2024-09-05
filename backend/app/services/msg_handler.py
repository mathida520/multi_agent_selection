def process_msgs(responses):
    msgs = []
    color = '#3498db'

    for response in responses:
        model = response["model"]
        msgs.append({
            "model": model,
            "message": response["message"],
            "color": color
        })
        if model == "llama3.1":
            pass
        else:
            msgs.append({
                'model': model,
                'message': response['response']['choices'][0]['message']['content'],
                'color': color,
            })

    return msgs

