from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_visit():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.XPATH, "//*[@id='user-name']")
        driver.find_element(By.XPATH, "//*[@id='password']")
        driver.find_element(By.XPATH, "//*[@id='login-button']")
    except NoSuchElementException:
        assert False
    assert True
    print("Элементы найдены")



