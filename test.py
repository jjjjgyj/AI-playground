import requests 
from bs4 import BeautifulSoup

# Define the URL of the web page you want to crawl
url = "https://pointstalent.com/"

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all title elements in the HTML
    elements = soup.find_all("div")
    
    # Extract the text of the title elements containing "points"
    filtered_elements = [element.text for element in elements if "达美" in element.text]  
    
    # Print the titles
    for filtered_element in filtered_elements:
        print(filtered_element)
else:
    print("Failed to retrieve the web page")
