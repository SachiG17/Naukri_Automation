import time

from selenium import webdriver
from pynput.keyboard import Key,Controller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#serv_obj = Service('C:/Users/Sachin/PycharmProjects/testselenium/Driver/chromedriver/chromedriver.exe')
#driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()

driver.implicitly_wait(15)
chrome_options = Options()
chrome_options.add_argument("--disable-cookies")
driver.get("https://www.naukri.com/")
driver.maximize_window()

driver.find_element(By.ID,"login_Layer").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter your active Email ID / Username']").send_keys("sachinghanteppagol17@gmail.com")
driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']").send_keys("Allthebest@2025")

driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//div[@class='nI-gNb-drawer__icon']").click()
driver.find_element(By.LINK_TEXT,"View & Update Profile").click()
upload_button = driver.find_element(By.XPATH,"//input[@type='file']")
#upload_button = driver.find_element(By.XPATH,"//input[@value='Update resume']")

driver.execute_script("arguments[0].style.display='block';", upload_button)
#filepath = ("C:\\Users\\Sachin\\Downloads\\SachinG_Automationtester.pdf")
upload_button.send_keys("C:\\Users\\Sachin\\PycharmProjects\\NaukriUpdate\\SachinG_Automationtester.pdf")
assert driver.find_element(By.XPATH,"//p[contains(text(),'Resume has been successfully uploaded.')]").is_displayed()
print("Sucessfully uploaded")

time.sleep(20)
driver.close()
