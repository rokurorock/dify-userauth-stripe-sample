import os
import requests
import json


def post_chat_message(inputs, query, user, conversation_id="", response_mode="streaming", file_url=None):
    api_key = os.getenv("DIFY_API_KEY")
    root_url = os.getenv("ROOT_URL")
    url = os.path.join(root_url, "v1/chat-messages")
    if not api_key:
        raise ValueError("API key is missing. Please set DIFY_API_KEY in your .env file.")

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    data = {"inputs": inputs, "query": query, "response_mode": response_mode, "conversation_id": conversation_id, "user": user, "files": []}

    if file_url:
        data["files"].append({"type": "image", "transfer_method": "remote_url", "url": file_url})

    response = requests.post(url, headers=headers, json=data, stream=True)

    for chunk in response.iter_lines():
        try:
            if chunk:
                j = json.loads(chunk.decode()[6:])
                yield j
        except Exception as e:
            print("error", e)
