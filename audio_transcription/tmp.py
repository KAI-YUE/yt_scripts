import os
import requests
import numpy as np
import cv2
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://images.google.com/")


keyword = "puppies"

# Create a directory to save downloaded images
download_dir = f"/mnt/ssd/Pictures/YT_sources/{keyword}"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)


# Find the search bar and enter the keyword
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
search_box.send_keys(keyword)
search_box.send_keys(Keys.ENTER)


num_images = 2
with_ads_x_path_format = "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[2]/div[1]/div[1]/span/div[1]/div[1]/div[{:d}]/a[1]"
without_ads_x_path_format = "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{:d}]/a[1]/div[1]"

with_ads_zoom_in_xpath = "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]"
without_ads_zoom_in_xpath = "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

for i in range(num_images+10):
    try:
        images = driver.find_element(By.XPATH, with_ads_x_path_format.format(i+1))
        images.click()
        time.sleep(2)
        detailed_img = driver.find_element(By.XPATH, with_ads_zoom_in_xpath)
    except:
        images = driver.find_element(By.XPATH, without_ads_x_path_format.format(i+1))
        images.click()
        time.sleep(2)
        detailed_img = driver.find_element(By.XPATH, without_ads_zoom_in_xpath)

    driver.maximize_window()

    try:
        img_url = detailed_img.get_attribute('src')
        r = requests.get(img_url, headers=headers)
    except:
        detailed_img = driver.find_element(By.XPATH, without_ads_zoom_in_xpath)
        img_url = detailed_img.get_attribute('src')
        r = requests.get(img_url, headers=headers)

    img_code = np.asarray(bytearray(r.content), dtype='uint8')
    img_arr = cv2.imdecode(img_code, cv2.IMREAD_COLOR)

    cv2.imwrite(f"{download_dir}/{i+1}.jpg", img_arr)


    



