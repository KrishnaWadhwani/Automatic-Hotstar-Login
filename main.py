from selenium import webdriver

import pyautogui

driver = webdriver.Chrome("chromedriver")#Put Full Path To Chrome Driver

driver.get("https://www.hotstar.com")

##driver.find_element_by_id("searchField").send_keys("Movies")
##
##pyautogui.hotkey('enter')

driver.find_element_by_xpath("//div[@class='signIn']").click()

driver.find_element_by_xpath("//div[@class='email-fb-button']").click()

driver.find_element_by_id("emailID").send_keys("Put Your Mail-Id Here")

driver.find_element_by_xpath("//button[@class='submit-button']").click()

driver.find_element_by_name("phoneNo").send_keys("Put Your Phone Number Here")

driver.find_element_by_xpath("//button[@class='submit-button']").click()

