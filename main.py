from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import time

# Chrome options to ignore SSL certificate errors
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# time.sleep(5)

# Open the Wi-Fi login page (which might have SSL issues)
driver.get("https://10.50.0.100:6081/php/uid.php?vsys=1&rule=0")

# Find and fill the username and password fields
if(driver.title == "Authentication Portal"):
    username_field = driver.find_element(By.NAME, "user")
    password_field = driver.find_element(By.NAME, "passwd")
    username_field.send_keys("bt2k21ec146")
    password_field.send_keys("NARE3465")
    password_field.send_keys(Keys.RETURN)
    if(driver.find_element(By.TAG_NAME, "p").text == "User Authenticated"):
        print("Success")
    else:
        print("Failed")

# time.sleep(5)

driver.quit()
