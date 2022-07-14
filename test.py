
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\\Users\\macharya\\Downloads\\chromedriver")
driver = webdriver.Chrome(service =service_obj)
driver.get("https://yahoo.com")


