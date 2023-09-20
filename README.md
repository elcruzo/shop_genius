# Shop Genius

Shop Genius is a web crawler and price tracking tool for gathering product information across multiple e-commerce websites. It allows users to make more cost-effective purchasing choices by providing price alerts and product details.

## Table of Contents

- [Shop Genius](#shop-genius)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)

## Features

- **Web Crawling**: Shop Genius uses Python and Scrapy to crawl and scrape data from popular e-commerce websites such as Amazon, Temu, and Shein.

- **Price Tracking**: Users can set price alerts for specific products, receiving notifications when the prices drop below their defined thresholds.

- **User Authentication**: The application includes user authentication to manage preferences and track product alerts for individual users.

- **Database Integration**: Shop Genius integrates with a database to store product data and user preferences.

- **Periodic Price Scraping**: The application periodically scrapes prices from e-commerce websites using a Scrapy spider, ensuring that users receive up-to-date information.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/elcruzo/shop_genius.git
   ```

2. Install the Scrapy Library:

   ```bash
   pip install scrapy
   ```

3. Install the Flask package:

   ```bash
   pip install Flask
   ```

4. Install the Flask authentication package:

   ```bash
   pip install Flask-Login
   ```
 
