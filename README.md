# Books To Scrape - Scraping: Basic Version (V1)

This is a simple Python script to scrape book data from [Books to Scrape](https://books.toscrape.com/), a website that provides a collection of books. The scraper collects details about the books, including itles, prices, ratings, availability, and cover image URLs. It stores the data into a CSV file.

## Features

- Scrapes book title, price, availability, rating, and image URL from the site [Books to Scrape](https://books.toscrape.com/).
- Supports scraping multiple pages.
- Saves the scraped data to a CSV file.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/username/book-scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd book-scraper
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate Virtual Environment:

   ```bash
   source venv/bin/activate # On Linux
   venv\Scripts\activate # On Windows
   ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script to start scraping:

1. On Python:

   ```bash
   python WebScraping.py
   ```

2. On Notebook:

   ```bash
   jupyter notebook

   ```

## License

[MIT LICENSE](LICENSE)

&copy;2024 Ryan Gading Abdullah. All rights reserved.
