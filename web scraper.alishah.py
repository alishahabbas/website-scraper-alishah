import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send a GET request to fetch the raw HTML content
        print("Fetching URL:", url)  # Debugging line
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Extract the title of the page
        page_title = soup.title.string if soup.title else "No title found"
        print(f"Page Title: {page_title}")

        # Example: Extract all the hyperlinks on the page
        links = soup.find_all('a', href=True)  # Find all anchor tags with href attributes
        print(f"\nFound {len(links)} links:")
        for link in links:
            print(link['href'])

        # Example: Extract all paragraphs on the page
        paragraphs = soup.find_all('p')
        print(f"\nFound {len(paragraphs)} paragraphs:")
        for paragraph in paragraphs:
            print(paragraph.get_text())

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching the URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
url = input("Enter the URL to scrape: ")  # Prompt for a URL to scrape
scrape_website(url)