import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#unshih
# df = pd.read_excel("test")

#setup
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

#login
driver.get("https://gp.garage.mn/parts")
time.sleep(1)

loginbttn = driver.find_element(By.ID, "btnlogin")
loginbttn.click()

driver.find_element(By.ID, "email").send_keys("ankhbayar@garage.mn")
driver.find_element(By.ID, "password").send_keys("Ankhaa#123", Keys.RETURN)

driver.get("https://gp.garage.mn/parts")

