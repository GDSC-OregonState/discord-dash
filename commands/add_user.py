import os
import requests

def add_user(username):
    api_token = os.getenv("GITHUB_API_TOKEN") 
    url = f"https://api.github.com/orgs/GDSC-OregonState/memberships/{username}" 
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    json = {"role": "member"}
    response = requests.put(url, headers=headers, json=json)

    if (response.status_code == 200):
        return f"User: {username} was added to the Github Org!!"
    else:
        return f"Failed to add user!! This was due to the following reasons: {response.json()}"