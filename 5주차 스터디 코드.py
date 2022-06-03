from unittest import result
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib import request
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
url = "https://pokemonkorea.co.kr/pokedex"
driver.implicitly_wait(3)
driver.get(url)
imgs = []
result = []
if not os.path.isdir(r'C:\Users\김효찬\Desktop\파이썬용\파이썬 폴더\스터디\스터디5주차\imgs'):
    os.mkdir(r'C:\Users\김효찬\Desktop\파이썬용\파이썬 폴더\스터디\스터디5주차\imgs')
imgs= driver.find_elements(By.CLASS_NAME,'tumb-wrp')
scroll_location = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    scroll_height=driver.execute_script("return document.body.scrollHeight")
    print(scroll_height)
    if scroll_height == 67708:
        break
    else:
        scroll_location = driver.execute_script("return document.body.scrollHelight")
for img in imgs:
    result.append(img.get_attribute('scr'))
for index, link in enumerate(result):
    request.urlretrieve(link,imgs.format(index, 'png'))