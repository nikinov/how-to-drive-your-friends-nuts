number = "607072587"
password = "somethingnew"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

path = "/Volumes/SSDexternal/OSX/nicholasnovelle/other/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath('//*[@id="email"]').send_keys(number)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[4]/div[1]/div[3]/span/div/div[1]').click()
sleep(5)
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div').click()
sleep(5)
input = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[4]/div[1]/div[1]/div[1]/div/div/div[1]/div/div/div/div[2]/div/div[2]/form/div/div[4]/div[2]/div[1]/div/div/div/div/div[2]/div')
input.click()
while True:
    input.send_keys("hey this is a bot")
    input.send_keys(Keys.ENTER)
    sleep(.1)









































