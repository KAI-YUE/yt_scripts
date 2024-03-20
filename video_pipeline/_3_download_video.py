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

import shutil

series_num = 22
prefix = "/mnt/ssd/Pictures/YT_source_vd/{:d}".format(series_num)

def read_keywords():
    # keyword = "puppies"
    
    # read key words from a txt file
    # Define the path to your document
    file_path = '/home/kyue/Projects/YT/audio_transcription/keyword.txt'
    
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


# def main():

downloads_folder = "/home/kyue/Downloads/"



if not os.path.exists(prefix):
    os.mkdir(prefix)

h, w = 1080, 1920


# driver.get("https://images.google.com/")

keywords = read_keywords()
# search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')


search_box_xpath = "/html/body/div[2]/div/div[2]/nav/div[1]/form/div/input"
search_box = None



for kk, keyword in enumerate(keywords):
    
    tmp_query = keyword.replace(" ", "%20")
    driver = webdriver.Chrome()
    driver.get("https://www.pexels.com/search/videos/{:s}".format(tmp_query))
    driver.maximize_window()

    
    time.sleep(2)
    
    # Create a directory to save downloaded images
    download_dir = os.path.join(prefix, "_{:d}_{:s}".format(kk, keyword))
    print(download_dir)
    if not os.path.exists(download_dir):
        print("mkdir")
        os.mkdir(download_dir)
        
    
    print(keyword)
    # download_x_path_format = "/html/body/div[2]/div/main/div[5]/div[1]/div/div[2]/div[1]/article/div[1]/a"
    # download_x_path_format = "/html/body/div[2]/div/main/div[4]/div[1]/div/div[2]/div[1]/article/div[1]/a/span/svg/use"
    download_xpath = "/html/body/div[2]/div/main/div[4]/div[1]/div/div[2]/div[1]/article/div[1]/a/span/span/span"
                   # /html/body/div[2]/div/main/div[4]/div[1]/div/div[2]/div[1]/article/div[1]/a/span/span/span
    album_xpath = "/html/body/div[2]/div/main/div[4]/div[1]/div/div[2]/div[1]/article/a/video"
    
    try:
        
        driver.execute_script('window.scrollBy(0, 200)')
        
        a = ActionChains(driver)
        m= driver.find_element(By.XPATH, album_xpath)
        a.move_to_element(m).perform()

        time.sleep(2)

        videos = driver.find_element(By.XPATH, download_xpath)
        # videos = driver.find_element(By.CLASS_NAME, "DownloadButton_downloadButtonText__qVWuI")
        videos.click()
        time.sleep(9)
    except:
        continue
    
    # break

    # search_box = driver.find_element(By.XPATH, search_box_xpath)
    # search_box.clear()
    
    # move it to the designated folder
    # List all files in the Downloads folder
    files = os.listdir(downloads_folder)
    
    # Find the generated .mp4 file
    for file in files:
        if file.endswith('.mp4'):
            source_path = os.path.join(downloads_folder, file)
            destination_path = os.path.join(download_dir, file)
            
            # Move the file
            shutil.move(source_path, destination_path)
            
            # Optional: Print confirmation
            print(f"Moved '{file}' to {download_dir}")
            break  # Assuming only one .mp4 file is generated per iteration
    
    driver.close()
    del driver
                                                                                                                                

exit()

# if __name__ == "__main__":
#     main()



