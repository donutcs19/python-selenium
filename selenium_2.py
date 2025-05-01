from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Create Webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#Open Website
driver.get("https://shikikie.netlify.app/")

element_name = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/h1").text 
element_title = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/h3").text  

print(f"name : {element_name}, title : {element_title}")

driver.quit()