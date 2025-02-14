import re
import time
import json
import requests
import dns.resolver
from selenium import webdriver

DOMAIN = "i-spy.chall.lac.tf"
HOST = f"https://{DOMAIN}"

session = requests.Session()


###########################
######### Step 01 #########
###########################
response = requests.post(f"{HOST}/api/suggestion")
token = json.loads(response.text)["suggestion"].split(" ")[-1]
print(json.loads(response.text))
print(token, end="\n\n")

response = session.post(f"{HOST}/api/suggestion", data={"stage_token": token})
time.sleep(1)  # for prevent too many requests


###########################
######### Step 02 #########
###########################
print(json.loads(response.text))
html = requests.get(f"{HOST}")
token = re.search(r"<!-- Token: (.*) -->", html.text).group(1)
print(token, end="\n\n")

response = session.post(f"{HOST}/api/suggestion", data={"stage_token": token})
time.sleep(1)  # for prevent too many requests


###########################
######### Step 03 #########
###########################
print(json.loads(response.text))
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
driver = webdriver.Chrome(options=options)
driver.get(HOST)
atoken = driver.get_cookies()[0]["value"]  # For step 7
logs = driver.get_log("browser")
token = re.search(r'"Token: (.*)"', logs[0]["message"]).group(1)
print(token, end="\n\n")

response = session.post(f"{HOST}/api/suggestion", data={"stage_token": token})
time.sleep(1)  # for prevent too many requests


###########################
######### Step 04 #########
###########################
print(json.loads(response.text))
response = requests.get(f"{HOST}/styles.css")
token = re.search(r"/\* Token: (.*) \*/", response.text).group(1)
print(token, end="\n\n")

response = session.post(f"{HOST}/api/suggestion", data={"stage_token": token})
time.sleep(1)  # for prevent too many requests


###########################
######### Step 05 #########
###########################
print(json.loads(response.text))
response = requests.get(f"{HOST}/thingy.js")
token = re.search(r"// Token: (.*)", response.text).group(1)
print(token, end="\n\n")

response = session.post(f"{HOST}/api/suggestion", data={"stage_token": token})
time.sleep(1)  # for prevent too many requests


###########################
######### Step 06 #########
###########################
print(json.loads(response.text))
token = response.headers["X-Token"]
print(token, end="\n\n")

response = session.post(f"{HOST}/api/suggestion", data={"stage_token": token})
time.sleep(1)  # for prevent too many requests


###########################
######### Step 07 #########
###########################
print(json.loads(response.text))
token = atoken
print(token, end="\n\n")

response = session.post(f"{HOST}/api/suggestion", data={"stage_token": token})
time.sleep(1)  # for prevent too many requests


###########################
######### Step 08 #########
###########################
print(json.loads(response.text))
response = requests.get(f"{HOST}/robots.txt")
disallow = re.search(r"Disallow: (.*)", response.text).group(1)
print(disallow)
time.sleep(1)  # for prevent too many requests
response = requests.get(f"{HOST}{disallow}")
token = re.search(r"Token: (.*)", response.text).group(1)
print(token, end="\n\n")

time.sleep(2)  # for prevent too many requests
response = session.post(f"{HOST}/api/suggestion", data={"stage_token": token})
time.sleep(1)  # for prevent too many requests


###########################
######### Step 09 #########
###########################
print(json.loads(response.text))
response = requests.get(f"{HOST}/sitemap.xml")
token = re.search(r"<!-- Token: (.*) -->", response.text).group(1)
print(token, end="\n\n")

time.sleep(1)  # for prevent too many requests
response = session.post(f"{HOST}/api/suggestion", data={"stage_token": token})
time.sleep(1)  # for prevent too many requests


###########################
######### Step 10 #########
###########################
print(json.loads(response.text))
response = requests.delete(f"{HOST}/")
token = response.text.split(" ")[-1]
print(token, end="\n\n")

time.sleep(1)  # for prevent too many requests
response = session.post(f"{HOST}/api/suggestion", data={"stage_token": token})
time.sleep(1)  # for prevent too many requests


###########################
######### Step 11 #########
###########################
print(json.loads(response.text))
txt_records = dns.resolver.resolve(DOMAIN, "TXT")
for record in txt_records:
    token = re.search(r'"Token: (.*)"', record.to_text()).group(1)
print(token, end="\n\n")

time.sleep(1)  # for prevent too many requests
response = session.post(f"{HOST}/api/suggestion", data={"stage_token": token})
time.sleep(1)  # for prevent too many requests


############################
#########   FLAG   #########
############################
print(json.loads(response.text))
flag = re.search(r"(lactf\{.*\})", response.text).group(1)
print(flag)
