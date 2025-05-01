from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

myProvince = ["เชียงใหม่", "น่าน", "สมุทรปราการ"]

for i in myProvince:
    print(f"\nค้นหาข้อมูลสำหรับจังหวัด: {i}")

    driver = webdriver.Chrome()
    driver.get("https://th.trovit.com/")

    # เข้าหมวดหมู่ "อสังหา"
    go_to_search = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#main > div > div.verticals > ul > li:nth-child(1) > a'))
    )
    go_to_search.click()

    # ค้นหาชื่อจังหวัด
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#what_d'))
    )
    search_box.send_keys(i)

    btn_search = driver.find_element(By.CSS_SELECTOR, '#search > button')
    btn_search.click()

    # รอให้รายการประกาศโหลด
    try:
        listings = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article"))
        )
        first_listing = listings[0]

        title = first_listing.find_element(By.CSS_SELECTOR, ".snippet-listing-content-header-title-left > span").text
        price = first_listing.find_element(By.CSS_SELECTOR, ".snippet-listing-content-header-title-right span").text

        print(f"{title} / ราคา: {price} THB")
    except Exception as e:
        print("❌ ไม่พบข้อมูลหรือโหลดไม่ทัน:", str(e))

    driver.quit()
