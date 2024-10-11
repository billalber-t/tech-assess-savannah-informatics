import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def browser():
    # Set up the Chrome driver
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_open_link(browser):
    # Open the specified link
    browser.get("https://8cc45a05-734d-439a-8adf-2feece2e0f60-00-2eh0vcpljane0.riker.replit.dev/")

    # Wait for a few seconds to let the page load

    time.sleep(5)

    # Example test: Check if the title contains a specific keyword
    assert "Web Application" in browser.title  # Change 'Expected Title' to the actual title you expect


def open_link_in_browser(browser):
    # Open the specified link
    browser.get("https://8cc45a05-734d-439a-8adf-2feece2e0f60-00-2eh0vcpljane0.riker.replit.dev/")



def test_search_item(browser):

    open_link_in_browser(browser)
    time.sleep(4)

    email = browser.find_element(By.ID, "email")
    email.send_keys("ruthmusyoka@gmail.com")
    browser.find_element(By.ID, "password").send_keys("RuthMusyoka100%")

    time.sleep(2)
    browser.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    time.sleep(2)
    browser.find_element(By.XPATH, "//a[normalize-space()='Albums']").click()

    time.sleep(2)
    browser.find_element(By.ID, "albumSearch").send_keys("quidem")

    browser.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
    time.sleep(3)

    para = browser.find_element(By.XPATH, "//div[@id='app']//div[1]//p[1]")
    assert "quidem" in para.text





if __name__ == "__main__":
    pytest.main()
