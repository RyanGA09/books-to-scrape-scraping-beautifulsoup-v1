import requests
from bs4 import BeautifulSoup
import csv
import time

# Function for scraping data from each page
def scrape_books_from_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Taking all the books
    books = soup.find_all('article', class_='product_pod')
    book_data = []

    for book in books:
        # Retrieving book titles
        title = book.h3.a['title']

        # Taking the book price
        price = book.find('p', class_='price_color').text

        # Retrieve book availability
        availability = book.find('p', class_='instock availability').text.strip()

        # Taking book ratings
        rating_class = book.p['class']
        rating = rating_class[1] if len(rating_class) > 1 else "No rating"

        # Retrieve cover image URL
        image_url = book.find('img')['src']
        image_url = 'https://books.toscrape.com/' + image_url.replace('../', '')

        # Store book data in dictionary form
        book_data.append({
            'Title': title,
            'Price': price,
            'Availability': availability,
            'Rating': rating,
            'Image URL': image_url
        })

    return book_data

# Function for scraping from multiple pages
def scrape_multiple_pages(base_url, total_pages):
    all_books = []

    for page in range(1, total_pages + 1):
        if page == 1:
            url = base_url  # First page
        else:
            url = f"{base_url}catalogue/page-{page}.html"  # Next page
        print(f"Scraping page {page}: {url}")
        books = scrape_books_from_page(url)
        if books:
            all_books.extend(books)
        time.sleep(1)  # Giving pause to avoid too many requests

    return all_books

# Function to save scraping result to CSV file
def save_to_csv(data, filename):
    if not data:
        print("No data to save.")
        return

    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    base_url = 'https://books.toscrape.com/'
    total_pages = 5  # Change this according to the number of pages you want to scrape
    books_data = scrape_multiple_pages(base_url, total_pages)
    save_to_csv(books_data, 'books_data.csv') 