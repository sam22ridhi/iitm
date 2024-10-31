import requests
import pandas as pd

# Replace 'YOUR_GITHUB_TOKEN_HERE' with your personal GitHub token
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN_HERE'

# Set up the GitHub API URL to find users in Sydney with over 100 followers
API_URL = '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'

# Set up headers with authorization
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}"
}

# Send a GET request to the GitHub API
response = requests.get(API_URL, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    users_data = response.json()['items']  # Get the list of users

    # Create a list to store the user data
    users = []
    for user in users_data:
        user_info = {
            'login': user['login'],
            'url': user['url'],
            'followers_url': user['followers_url'],
            'repos_url': user['repos_url']
        }
        users.append(user_info)

    # Convert list to DataFrame and save it to users.csv
    users_df = pd.DataFrame(users)
    users_df.to_csv('users.csv', index=False)
    print("Saved users.csv!")
else:
    print("Failed to fetch users:", response.status_code)
