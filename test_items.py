import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_online_store(browser):
    browser.get(link)
    element = browser.find_element_by_css_selector("button.btn.btn-primary")
    result = element.text
    time.sleep(15)
    assert len(result) != 0, f"Expected not zero value, got '{result}'"