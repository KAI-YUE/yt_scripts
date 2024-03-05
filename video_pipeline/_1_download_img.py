import os
import requests
import numpy as np
import cv2
import time

from threading import Thread

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import threading
from threading import Thread


def read_keywords():
    # keyword = "puppies"
    
    # read key words from a txt file
    # Define the path to your document
    file_path = '/home/kyue/Projects/YT/audio_transcription/_1_eden_keyword.txt'
    
    # Initialize an empty list to hold the keywords
    keywords = []
    
    # Open the document and read its contents
    with open(file_path, 'r') as file:
        for line in file:
            # Strip newline characters and any leading/trailing whitespace
            keyword = line[:-10]
            # Add the keyword to the list
            if keyword:  # This checks that the line is not empty
                keywords.append(keyword)
    
    # Print the list of keywords
    # print(keywords)
    return keywords
    

def download_from_url(detailed_img):
    
    print("hello")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    img_url = detailed_img.get_attribute('src')
    r = requests.get(img_url, headers=headers)

    img_code = np.asarray(bytearray(r.content), dtype='uint8')
    img_arr = cv2.imdecode(img_code, cv2.IMREAD_COLOR)

    return img_arr


def run_with_timeout(func, args=(), kwargs={}, timeout_duration=10):
    class FunctionThread(threading.Thread):
        def __init__(self):
            super().__init__()
            self.result = None

        def run(self):
            self.result = func(*args, **kwargs)

    # Create a thread to run the function
    func_thread = FunctionThread()
    func_thread.start()
    # Wait for the function to finish or timeout
    func_thread.join(timeout_duration)
    if func_thread.is_alive():
        # The function is still running, it's time to stop it
        raise TimeoutError("Function timed out")
    else:
        return func_thread.result


def main():
    
    series_num = 1
    offset = 10
    prefix = "/mnt/ssd/Pictures/YT_sources/{:d}".format(series_num)
    if not os.path.exists(prefix):
        os.mkdir(prefix)

    h, w = 1080, 1920
    
    driver = webdriver.Chrome()
    driver.get("https://images.google.com/")
    
    output_folder = "/mnt/ssd/Pictures/YT_sources/"
    
    keywords = read_keywords()
    search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
    
    for kk, keyword in enumerate(keywords):
    
        # Create a directory to save downloaded images
        download_dir = os.path.join(prefix, "_{:d}_{:s}".format(kk, keyword))
        print(download_dir)
        if not os.path.exists(download_dir):
            print("mkdir")
            os.mkdir(download_dir)
            
        
        print(keyword)
        
        # Find the search bar and enter the keyword
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
        
        num_images = 1
        with_ads_x_path_format = "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[2]/div[1]/div[1]/span/div[1]/div[1]/div[{:d}]/a[1]"
        without_ads_x_path_format = "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{:d}]/a[1]/div[1]"
        
        with_ads_zoom_in_xpath = "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]"
        without_ads_zoom_in_xpath = "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]"
        
        num_valid_imgs = 0
        for i in range(num_images+offset):
            try:
                images = driver.find_element(By.XPATH, with_ads_x_path_format.format(i+1))
                images.click()
                time.sleep(2)
                detailed_img = driver.find_element(By.XPATH, with_ads_zoom_in_xpath)
            except:
                try:
                    images = driver.find_element(By.XPATH, without_ads_x_path_format.format(i+1))
                    images.click()
                    time.sleep(2)
                    detailed_img = driver.find_element(By.XPATH, without_ads_zoom_in_xpath)
                except:
                    continue            


            if i == 0 and kk == 0:
                driver.maximize_window()
            
            # set a time out func 
            output_src = os.path.join(download_dir, "{:d}.jpg".format(i))
            print(output_src)
            
            try:
                img_arr = run_with_timeout(download_from_url, args=(detailed_img, ), timeout_duration=5)
                resized = resize_and_pad(img_arr, w, h)
                cv2.imwrite(output_src, resized)
                num_valid_imgs += 1
            except:
                continue
            
            if num_valid_imgs > num_images:
                break

        search_box = driver.find_element(By.XPATH, '/html/body/c-wiz/c-wiz/div/div[3]/div[2]/div/div[1]/form/div[1]/div[2]/div/div[2]/input')
        search_box.clear()            

    exit()

def resize_and_pad(img_arr, width, height):
    # Calculate the target aspect ratio
    target_aspect = width / height
    
    # Calculate the aspect ratio of the input image
    img_h, img_w = img_arr.shape[:2]
    img_aspect = img_w / img_h
    
    # Determine the padding values
    if img_aspect < target_aspect:
        # The image is taller than the target aspect ratio, pad horizontally
        new_width = int(target_aspect * img_h)
        padding = (new_width - img_w) // 2
        padded_img = cv2.copyMakeBorder(img_arr, 0, 0, padding, padding, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    else:
        # The image is wider than the target aspect ratio, pad vertically
        new_height = int(img_w / target_aspect)
        padding = (new_height - img_h) // 2
        padded_img = cv2.copyMakeBorder(img_arr, padding, padding, 0, 0, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    
    # Resize the padded image to the target dimensions
    resized_img = cv2.resize(padded_img, (width, height))
    
    return resized_img

if __name__ == "__main__":
    main()



