from selenium.webdriver.common.by import By
import time


def test_item_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    browser.get(link)
    basket = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button')
    time.sleep(5)
    assert basket.is_displayed()
