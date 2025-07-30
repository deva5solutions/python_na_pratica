from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Substitua o caminho do driver se necessário
driver = webdriver.Chrome()
driver.get("https://www.google.com")

search = driver.find_element(By.NAME, "q")
search.send_keys("Python")
search.submit()
