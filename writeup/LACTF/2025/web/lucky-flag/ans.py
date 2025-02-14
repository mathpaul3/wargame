from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm

HOST = "https://lucky-flag.chall.lac.tf"

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)
driver.get(f"{HOST}/")
driver.implicitly_wait(10)

elements = driver.find_elements(By.TAG_NAME, "button")
print(len(elements))

for idx, element in tqdm(enumerate(elements)):
    try:
        element.click()
        text = driver.switch_to.alert.text
        if text != "no flag here":
            print(idx, text)
            break
        driver.switch_to.alert.accept()
    except:
        pass
driver.quit()
