# Price Tracking Application

This application tracks prices of selected products on Amazon India using web scraping. It fetches the current price of each product and compares it with your target price. If the current price is below the target price, it logs the product name and the price.

## Prerequisites

- Python 3.x
- `requests` library: `pip install requests`
- `beautifulsoup4` library: `pip install beautifulsoup4`

## Usage

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Update the products list:**
   Modify the `products_list` in the script to include the URLs and target prices of the products you want to track.

4. **Run the script:**
   ```bash
   python price_tracking.py
   ```

   The script will fetch the current prices of the products and compare them with the target prices. If a product is available at or below the target price, it will be logged in `result_file.txt`.

## Example

Here's a list of products being tracked and their target prices:

| Product Name              | Target Price (INR) |
|---------------------------|--------------------|
| Samsung Galaxy S24 FE     | 40000              |
| Samsung Galaxy S23 Ultra  | 80000              |
| Samsung Galaxy S21 FE     | 40000              |
| Backlit LED Monitor       | 23000              |
| Length Jacket             | 1200               |

## How It Works

1. **Product List:** 
   A list of dictionaries containing the product URLs, names, and target prices.

2. **Fetching Price:**
   The `run_product_price` function sends a GET request to the product URL and uses BeautifulSoup to parse the HTML and extract the current price.

3. **Comparison:**
   The script compares the fetched price with the target price. If the fetched price is below the target price, it logs the product name and the price in `result_file.txt`.

4. **Output:**
   - If a product is available at or below the target price, it logs the result in `result_file.txt`.
   - Otherwise, it indicates that the product is still at the current price.

## Disclaimer

This script is for educational purposes only. Make sure to adhere to the website's terms of service and usage policies when using web scraping techniques.

## License

This project is licensed under the MIT License.
