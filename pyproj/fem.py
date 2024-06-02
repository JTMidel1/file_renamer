import requests
from bs4 import BeautifulSoup as bs
github_user = input('input Github User: ')
url = 'https://github.com/'+github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt' : 'Avatar'})[src]
if status_code == 200:
    print(profile_image) 
else:
    print("Error code")



...\
import requests
from bs4 import BeautifulSoup as bs

# Get GitHub username input
github_user = input('Input GitHub User: ')

# Construct the URL for the user's GitHub profile
url = 'https://github.com/' + github_user

# Perform the HTTP GET request
r = requests.get(url)

# Check if the request was successful (status code 200)
if r.status_code == 200:
    # Parse the content of the request with BeautifulSoup
    soup = bs(r.content, 'html.parser')

    # Find the image with the alt attribute 'Avatar'
    profile_image_tag = soup.find('img', {'alt': 'Avatar'})

    if profile_image_tag:
        # Extract the source URL of the profile image
        profile_image = profile_image_tag['src']
        print(profile_image)
    else:
        print("Profile image not found.")
else:
    print(f"Failed to retrieve the page. Status code: {r.status_code}")

/...