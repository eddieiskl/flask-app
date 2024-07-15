# Import the requests library to send HTTP requests
import requests

# Send a GET request to the GitHub API to retrieve the repositories of the user 'avielb'
response = requests.get("https://api.github.com/users/avielb/repos")

# Check if the status code of the response is 200, indicating the request was successful
if response.status_code == 200:
    # Print a message indicating GitHub is up
    print("github is up")

    # Convert the response to JSON format (list of dictionaries)
    repos = response.json()

    # Iterate through each repository in the list of repositories
    for repo in repos:
        # Check if the string "devops" is present in the repository name (case-insensitive)
        if "devops" in str(repo["name"]).lower():
            # If the condition is true, print the name of the repository
            print(repo["name"])
else:
    # If the status code is not 200, print an error message
    print("Failed to retrieve repositories")