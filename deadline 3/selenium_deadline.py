from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(2)

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # First product
    first = driver.find_element(By.CLASS_NAME, "inventory_item")
    first.click()

    time.sleep(2)

    # Add to Cart
    add = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add.click()

    time.sleep(2)

    # Go to cart
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    time.sleep(3)

finally:
    driver.quit()
