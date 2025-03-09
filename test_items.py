import pytest
from selenium.webdriver.common.by import By
import time

def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    # Проверяем наличие кнопки добавления в корзину
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "Button 'Add to basket' is not found"
