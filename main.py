import requests
from bs4 import BeautifulSoup
from lxml import etree
import json


# Hint - use https://myhttpheader.com/ to get your sample headers

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-Language':'en-US,en;q=0.9,he-IL;q=0.8,he;q=0.7'}
response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", headers=headers)

amazon_html = response.text
amazon_soup = BeautifulSoup(amazon_html, "lxml")

print(amazon_soup.prettify())

try:
    captca = amazon_soup.find(name="p", class_="a-last").get_text()
    print("cAPTCHA"+captca)
    if captca.startswith("Sorry"):
        print("Captcha")
except:
    print("No Captcha")
    price_symbol = amazon_soup.find(name="div", class_="a-section aok-hidden twister-plus-buying-options-price-data")
    print(price_symbol.text)
    price_dict = price_symbol.text
    parsed_data = json.loads(price_dict)
    display_price = parsed_data['desktop_buybox_group_1'][0]['displayPrice']
    print(display_price)

