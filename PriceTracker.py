import requests
from bs4 import BeautifulSoup

products_list = [
    {
        "product_url" : "https://www.amazon.in/Samsung-Galaxy-Smartphone-Graphite-Storage/dp/B0DHL7YT5S/ref=sr_1_9?sr=8-9",
        "Name" : "Samsung Galaxy S24 FE ",
        "target_price" : 40000
    },
    {
        "product_url": "https://www.amazon.in/Samsung-Galaxy-Ultra-Green-Storage/dp/B0BT9CXXXX/ref=sr_1_1_sspa?sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "Name" : "Samsung Galaxy S23 Ultra",
        "target_price" : 80000

    },
    {
        "product_url" : "http://amazon.in/Samsung-Galaxy-S21-FE-Snapdragon/dp/B0DKTLBFSB/ref=sr_1_9?sr=8-9",
        "Name" : "Samsung Galaxy S21 FE",
        "target_price" : 40000
    },
    {
        "product_url": "https://www.amazon.in/Acer-3840x2160-1xType-C-Certified-Speakers/dp/B0BFB4GZ4J/ref=sr_1_21_sspa?sr=8-21-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9idGY&psc=1",
        "Name": "Backlit LED Monitor",
        "target_price": 23000
    },
    {
        "product_url": "https://www.amazon.in/Amazon-Brand-Inkast-Lightweight-AW20-LW-INK-03_Black1_L/dp/B09FT54PWV/?_encoding=UTF8&ref_=pd_hp_d_btf_ci_mcx_mr_hp_atf_m",
        "Name": "Length Jacket",
        "target_price": 1200
    }
]

def run_product_price(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}

    page = requests.get(product_url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find("span", {"class": "a-price-whole"})

    return product_price.getText()


try:
    result_file = open('result_file.txt','w')
    for every_product in products_list:
        product_price_returned = run_product_price(every_product.get("product_url"))
        print("Rs " + product_price_returned + " - " + every_product.get("Name"))

        my_product = product_price_returned
        my_product = product_price_returned.replace(',', '')
        my_product = int(float(my_product))
        print(my_product)

        if my_product < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get("Name") + '\t' + "Available at your Target price - Rs." + str(my_product) + '\n')
        else:
            print("Still at current price")


finally:
    result_file.close()








