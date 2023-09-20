# Shop Genius

Shop Genius is a web crawler and price tracking tool for gathering product information across multiple e-commerce websites. It allows users to make more cost-effective purchasing choices by providing price alerts and product details.

## Table of Contents

- [Shop Genius](#shop-genius)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

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
 
5. Set up and configure the SQLite database:

Shop Genius uses SQLite as its database backend. You don't need to install a separate database server. SQLite is a lightweight, serverless database that stores data in a local file.

The SQLite database file is automatically created when you run the application for the first time. You can find the database file in the project directory with the name shop_genius.db.

6. Configure your email and Twilio credentials for sending price alerts in the `price_tracker.py` script.


## Usage

1. Run the application:

    ```python
    python app.py
    ```

2. Access the application through your web browser at `http://localhost:5000`

3. Register or log in to your account to start using Shop Genius.

4. Configure price alerts and track your favorite products.

## Contributing

Contributions are welcome! If you'd like to contribute to Shop Genius, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:
   
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add your commit message here"
   ```

4. Push your changes to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a pull request on the main repository.

## License

This project is licensed under the [LICENSE](LICENSE)) - see the LICENSE file for details.