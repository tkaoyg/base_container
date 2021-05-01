import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# File Name
# FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")
FILENAME = "C:/Users/ao/Desktop/image/screen.png"   # 指定のディレクトリはあらかじめ作成しておかないと保存されない

# set driver and url
driver = webdriver.Chrome('D:/chromedriver/chromedriver.exe')
url = 'http://www2.thr.mlit.go.jp/gassan/damu/main.html'
driver.get(url)

# get width and height of the page
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")

# set window size
driver.set_window_size(w,h)

# Get Screen Shot
driver.save_screenshot(FILENAME)

# Close Web Browser
driver.quit()