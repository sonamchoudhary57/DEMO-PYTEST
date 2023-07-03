import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def setup():
    # Set up the browser instance
    driver = webdriver.Chrome()  # Update with the appropriate driver for your browser
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Open the Cricbuzz website
    driver.get("https://www.cricbuzz.com")

    # Pass the driver instance to the tests
    yield driver

    # Teardown - close the browser
    driver.quit()

def test_home_page_title(setup):
    driver = setup
    assert driver.title == "Cricbuzz - Live Cricket Scores, Schedule, News, Archives, Series"

def test_search_bar(setup):
    driver = setup
    search_input = driver.find_element_by_id("search-query")
    search_input.send_keys("India vs England")
    search_input.submit()

    # Add more assertions or verifications related to the search functionality

def test_navigation_menu(setup):
    driver = setup
    # Perform actions on the navigation menu and verify expected behavior

    # Add more test cases for different features or sections of the website

