import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

EMAIL = "ankhbayar@garage.mn"
PASSWORD = "Ankhaa#123"

#unshih
df = pd.read_excel("TestArticle.xlsx")

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

driver.find_element(By.ID, "email").send_keys(EMAIL)
driver.find_element(By.ID, "password").send_keys(PASSWORD, Keys.RETURN)

#process
for index, row in df.iterrows():
    article_id = row['ArticleID']
    
    driver.get("https://gp.garage.mn/parts")
    time.sleep(1)
    
    driver.find_element(By.ID, "articleid").send_keys(str(article_id), Keys.RETURN)
    time.sleep(1)
    
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.text-body.fw-bold"))
    )
    link.click()
    
    #OEM huulah
    try:
        h5_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h5.text-truncate.font-size-14"))
        )

        part_number = h5_element.text.strip()
        print("Huulsan oem:", part_number)
    except Exception as e:
        print("Aldaatai articleId", str(row))