from time import sleep
from os import environ
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


load_dotenv()

service = Service(executable_path=environ["DRIVER"])
options = Options()
options.add_argument("--headless=new")
options.add_argument("--log-level=3")
driver = webdriver.Chrome(service=service, options=options)

URL_SIGNIN = "https://baharkargo.az/az/signin.html"
URL_PAGE_COUNT = "https://baharkargo.az/parcel/index?lang=az&status=7"

print("\nSigning In...")
driver.get(URL_SIGNIN)
close_add = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button/span")
close_add.click()
email = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/section/div/div/div[1]/form/div/div/div[1]/div[1]/input",
)
password = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/section/div/div/div[1]/form/div/div/div[1]/div[2]/input",
)
email.send_keys(environ["EMAIL"])
password.send_keys(environ["PASS"])
enter = driver.find_element(
    By.XPATH, "/html/body/div[1]/section/div/div/div[1]/form/div/div/div[2]/p/button"
)
enter.click()
sleep(1.2)
print("Getting pages...")
driver.get(URL_PAGE_COUNT)
sleep(1.2)
page_count = driver.find_element(By.CLASS_NAME, "pagination")
page_count = len(page_count.text.split()) - 2

all_items = []

for page in range(1, page_count + 1):
    print(f"Processing page {page}...")
    driver.get(f"{URL_PAGE_COUNT}&page={page}")
    sleep(1.2)

    card_items = driver.find_elements(By.CLASS_NAME, "card-item")
    for i in card_items:
        item = i.find_element(By.CLASS_NAME, "card-item__output").text
        if item:
            if "₼" in item:
                parts = item.split()
                dollar = float(parts[0].replace("$", ""))
                manat = float(parts[2])
                all_items.append((dollar, manat))

print(
    "\nPaketler :",
    (
        len([i[1] for i in all_items])
        if len([i[1] for i in all_items]) == len([i[0] for i in all_items])
        else None
    ),
)
print("Manat    :", round(sum([i[1] for i in all_items]), 2), "₼")
print("Dollar   :", round(sum([i[0] for i in all_items]), 2), "$")

driver.quit()
