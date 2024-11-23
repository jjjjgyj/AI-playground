import requests
from bs4 import BeautifulSoup
from typing import List, Optional

def get_webpage_content(url: str) -> Optional[BeautifulSoup]:
    """
    Fetch and parse webpage content from given URL.
    
    Args:
        url: The webpage URL to crawl
        
    Returns:
        BeautifulSoup object if successful, None otherwise
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except requests.RequestException as e:
        print(f"Failed to retrieve webpage: {e}")
        return None

def extract_filtered_text(soup: BeautifulSoup, tag: str, keyword: str) -> List[str]:
    """
    Extract text from elements containing specified keyword.
    
    Args:
        soup: BeautifulSoup object of parsed HTML
        tag: HTML tag to search for
        keyword: Text to filter elements by
        
    Returns:
        List of text from matching elements
    """
    elements = soup.find_all(tag)
    return [element.text for element in elements if keyword in element.text]

def main():
    url = "https://pointstalent.com/"
    soup = get_webpage_content(url)
    
    if soup:
        filtered_elements = extract_filtered_text(soup, "p", "达美")
        for element in filtered_elements:
            print(element)

if __name__ == "__main__":
    main()
