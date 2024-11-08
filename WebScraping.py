import requests
from bs4 import BeautifulSoup
import csv
import time

# Fungsi untuk scraping data dari setiap halaman
def scrape_books_from_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Memeriksa apakah permintaan berhasil
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Mengambil semua buku
    books = soup.find_all('article', class_='product_pod')
    book_data = []

    for book in books:
        # Mengambil judul buku
        title = book.h3.a['title']

        # Mengambil harga buku
        price = book.find('p', class_='price_color').text

        # Mengambil ketersediaan buku
        availability = book.find('p', class_='instock availability').text.strip()

        # Mengambil rating buku
        rating_class = book.p['class']
        rating = rating_class[1] if len(rating_class) > 1 else "No rating"

        # Mengambil URL gambar sampul
        image_url = book.find('img')['src']
        image_url = 'https://books.toscrape.com/' + image_url.replace('../', '')

        # Menyimpan data buku dalam bentuk dictionary
        book_data.append({
            'Title': title,
            'Price': price,
            'Availability': availability,
            'Rating': rating,
            'Image URL': image_url
        })

    return book_data

# Fungsi untuk scraping dari beberapa halaman
def scrape_multiple_pages(base_url, total_pages):
    all_books = []

    for page in range(1, total_pages + 1):
        if page == 1:
            url = base_url  # Halaman pertama
        else:
            url = f"{base_url}catalogue/page-{page}.html"  # Halaman berikutnya
        print(f"Scraping page {page}: {url}")
        books = scrape_books_from_page(url)
        if books:
            all_books.extend(books)
        time.sleep(1)  # Memberikan jeda untuk menghindari terlalu banyak request

    return all_books

# Fungsi untuk menyimpan hasil scraping ke file CSV
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
    total_pages = 5  # Ubah ini sesuai dengan jumlah halaman yang ingin di-scrape
    books_data = scrape_multiple_pages(base_url, total_pages)
    save_to_csv(books_data, 'books_data.csv') 