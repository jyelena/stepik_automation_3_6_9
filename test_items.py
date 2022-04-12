from selenium.webdriver.common.by import By


link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_add_to_basket_button(browser):
    browser.get(link)
    assert browser.find_element(
        By.CSS_SELECTOR, "button[class~='btn-add-to-basket']"
    ), "Page has no add_to_basket button"
