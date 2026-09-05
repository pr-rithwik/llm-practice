import json

from llm_practice.llm.artist import artist
from llm_practice.llm.talker import talker
from llm_practice.services.github_api import get_github_repo_stats


def handle_github_tool_calls(message):
    responses = []

    for tool_call in message.tool_calls:
        if tool_call.function.name == "get_github_repo_stats":
            print("Tool Call Usage: get_github_repo_stats")
            arguments = json.loads(tool_call.function.arguments)
            repo_url = arguments.get('repo_url')
            details = get_github_repo_stats(repo_url=repo_url)
            responses.append({
                "role": "tool",
                "content": json.dumps(details),
                "tool_call_id": tool_call.id
            })
    
    return responses


def handle_multi_modal_tool_calls(message):
    responses, cities = [], []
    image, voice = None, None

    for tool_call in message.tool_calls:
        if tool_call.function.name == "talker":
            print("Tool Call Usage: talker")
            arguments = json.loads(tool_call.function.arguments)
            message = arguments.get('message')
            voice = talker(message=message)
            responses.append({
                "role": "tool",
                "content": "Voice Generated Succesfully",
                "tool_call_id": tool_call.id
            })
        
        if tool_call.function.name == "artist":
            print("Tool Call Usage: artist")
            arguments = json.loads(tool_call.function.arguments)
            city = arguments.get('city')
            cities.append(city)
            image = artist(city=city)
            responses.append({
                "role": "tool",
                "content": "Image Generated Successfully",
                "tool_call_id": tool_call.id
            })
        
    details = {
        "cities": cities,
        "image": image,
        "voice": voice
    }
    return responses, details