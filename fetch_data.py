import requests
import csv

# Your GitHub token
GITHUB_TOKEN = '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'  # Replace with your actual token

# Set the API URL
API_URL = 'https://api.github.com/search/users?q=location:sydney+followers:>100'

# Set the headers with authorization
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}"
}

# Make the request to the GitHub API
response = requests.get(API_URL, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Prepare users.csv
    users = data.get('items', [])
    with open('users.csv', mode='w', newline='', encoding='utf-8') as users_file:
        users_writer = csv.writer(users_file)
        # Write the header
        users_writer.writerow(['login', 'name', 'company', 'location', 'email', 'hireable', 'bio', 'public_repos', 'followers', 'following', 'created_at'])
        
        for user in users:
            users_writer.writerow([
                user.get('login', ''),
                user.get('name', ''),
                user.get('company', '').strip('@').strip().upper(),
                user.get('location', ''),
                user.get('email', ''),
                user.get('hireable', False),
                user.get('bio', ''),
                user.get('public_repos', 0),
                user.get('followers', 0),
                user.get('following', 0),
                user.get('created_at', '')
            ])

    print("users.csv created successfully.")
else:
    print(f"Error fetching data from GitHub API: {response.status_code} - {response.text}")
