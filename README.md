# books-to-scrape-scraping

This is a simple Python script to scrape book data from [Books to Scrape](https://books.toscrape.com/), a website that provides a collection of books. The scraper collects details about the books, including title, price, availability, rating, and image URL. It stores the data into a CSV file.

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

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes. Please ensure that your contributions adhere to the existing style and coding standards.

Important: When contributing, please create a new branch for your changes instead of pushing directly to the main branch. To do this:

Create a new branch:

```bash
git checkout -b your-feature-branch
```

Make your changes and commit them:

```bash
git add .
```

```bash
git commit -m "Add a descriptive message about your changes"
```

Push the branch to your forked repository:

```bash
git push -u origin your-feature-branch
```

Open a pull request from your branch to the main branch of the original repository.

**_By following these guidelines, you help maintain a clean and manageable project history._**

## LICENSE

[MIT LICENSE](LICENSE)
&copy; 2024 Ryan Gading Abdullah. All rights reserved.
