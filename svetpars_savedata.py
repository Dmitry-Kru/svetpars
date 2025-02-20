import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/svet"
driver.get(url)
time.sleep(3)

svets = driver.find_elements(By.CSS_SELECTOR, 'div.WdR1o')

parsed_data = []

for item in svets:
    try:
        title = item.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        link_element = item.find_element(By.CSS_SELECTOR, "link[itemprop='url']")
        link = link_element.get_attribute("href")
        price = item.find_element(By.CSS_SELECTOR, "span[data-testid='price']").text

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([title, price, link])

driver.quit()

with open("svetilniki.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)
