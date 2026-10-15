from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

service = Service('chromedriver.exe')
driver = Chrome(service=service)
driver.get('https://www.vlr.gg/stats')
driver.find_element(by=By.XPATH,value='//*[@id="wrapper"]/div[1]/div/form/div[1]/label[1]/select').click()
time.sleep(1)
driver.find_element(By.XPATH,value='//*[@id="wrapper"]/div[1]/div/form/div[1]/label[1]/select/option[1]').click()
driver.find_element(By.XPATH,value='//*[@id="wrapper"]/div[1]/div/form/div[1]/button[2]').click()
time.sleep(1)
full_page_source = [driver.page_source]
for i in range(2,23):
    driver.get('https://www.vlr.gg/stats?sort=rating2&dir=desc&tier=all&region=all&span=60d&side=all&role=all&agent=all&map_id=all&min_rounds=100&min_rating=0&page={}'.format(i))
    full_page_source.append(driver.page_source)

for i in full_page_source:
    with open('vct_gg.html','a',encoding='utf-8') as f:
        f.write(i)




































input()