from typing import List, Dict

from openai import OpenAI

import random


def process_msgs(responses: List[Dict]) -> List[Dict]:
    msgs = []
    colors = ["#B5D9FE", "#F9C2C2", "#FFE195"]

    for response in responses:
        model = response.get("model", "")
        color = random.choice(colors)
        if model == "llama3.1":
            msgs.append({
                "model": model,
                "message": response.get("message", {}).get("content", ""),
                'images': response.get('images', []),
                "color": color
            })
        else:
            msgs.append({
                'model': model,
                'message': response.get('response', {}).get('choices', [{}])[0].get('message', {}).get('content', ""),
                'images': response.get('response', {}).get('choices', [{}])[0].get('images', []),
                'color': color,
            })
    return msgs
    
def sort_message(modellist,message_list,question):    
    MODEL = "gpt-4o"
    api_key = "sk-Av21e8b884d4106abc8c43ab02aee1279504f332491Ip2FS"
    messages=["{"+str(modellist[i])+":"+str(message_list[i])+"}" for i in range(len(modellist))]
    content ='请判断{}内的话哪个给符合提问&'+question+'&,请根据符合程度返回回答选项的模型名称的排序,只返回模型名称即可，输出格式为【模型名1，模型名2....】,'
    for i in range(len(message_list)): content=content+messages[i]
    # get response from GPT-4o

    client = OpenAI(api_key=api_key, base_url="https://api.gptsapi.net/v1")
    completion = client.chat.completions.create(
    model=MODEL,
    # temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Complete the following tasks carefully!"},
        # {"role": "system", "content": role_prompt},
        {"role": "user", "content": content}
        ]
    )
    
    return completion.choices[0].message.content

def resort_msgs(responses: List[Dict],question) -> List[Dict]:
    msgs = process_msgs(responses)
    modellist = [msgs[i]["model"] for i in range(len(msgs))] 
    message_list = [msgs[i]["message"] for i in range(len(msgs))] 
    
    return sort_message(modellist,message_list,question)

