import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://huntingpony.com"

def test_make_order():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # open Browser in maximized mode
    chrome_options.add_argument("--disable-infobars") # disabling infobars
    chrome_options.add_argument("--disable-extensions") # disabling extensions
    chrome_options.add_argument("--disable-gpu") #  applicable to windows os only
    chrome_options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
    # chrome_options.add_argument("--headless")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url=URL)

    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='banner-list__item-title']")
    element.click()

    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='lazyload product-preview__img-1 entered loaded']")
    element.click()

    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='add-cart-counter__btn-label']")
    element.click()

    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='button button_size-xl  add-cart-counter__controls-btn']")
    element.click()

    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='icon icon-cart']")
    element.click()

    sku = driver.find_element(By.XPATH, value="/html/body/div[1]/main/div/div/h1")

    assert sku.text == 'Корзина', "Unexpected sku"