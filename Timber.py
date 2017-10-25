#imports
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# create a new Chrome session
driver = webdriver.Chrome(executable_path='/whatever_your_ChromeDriver_path_is')
driver.implicitly_wait(30)
driver.maximize_window()

#Opening Tinder.com
driver.get("http://www.tinder.com")

#You get 60 seconds to log in to Tinder and skip the initial tutorial
time.sleep(60)

#Finding the like button
cl1 = driver.find_element_by_xpath('//*[@id="content"]/div/span/div/div[1]/div/main/div/div/div/div[1]/div[2]/button[3]')

#Infinite loop which clicks the "Like" button every second
while True:
    cl1.click()
    time.sleep(1)

#This part doesn't work yet. To terminate the script use the standard keyboard interrupt, i.e CTRL+C
if cv2.waitKey(1) & 0xFF  == ord('q'):
        driver.quit()
