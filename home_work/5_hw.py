from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def transion():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, "user > name")
    except NoSuchElementException:
        assert False
    assert print("Элементы найдены")


