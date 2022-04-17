from unittest import TestCase
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test(TestCase):
    def test_test_selenium(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.selenium.dev/documentation/webdriver/getting_started/install_library/")
        header = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/main/div/h1')
        title = driver.title
        self.assertTrue(expr=(header.text in title), msg=f"Title doesn't match the expected\n"
                                                         f"Expected: {title}\nFound: {header.text}")
        install_library = driver.find_element(By.ID, 'tabs-0-1-tab')
        install_library.send_keys(Keys.ENTER)
        page_browser_drivers = driver.find_element(By.LINK_TEXT, 'Install the browser drivers')
        page_browser_drivers.send_keys(Keys.ENTER)
        install_browser = driver.find_element(By.ID, 'quick-reference')
        install_browser_image = driver.get_screenshot_as_file(filename='selenium.png')
        install_browser_python = driver.find_element(By.ID, 'tabs-2-1-tab')
        install_browser_python.send_keys(Keys.ENTER)
        install_browser_bash = driver.find_element(By.ID, 'tabs-3-0-tab')
        install_browser_bash.send_keys(Keys.ENTER)
        install_browser_hard_code = driver.find_element(By.ID, 'tabs-4-1-tab')
        install_browser_hard_code.send_keys(Keys.ENTER)
        page_open_close_browser = driver.find_element(By.LINK_TEXT, 'Open and close a browser')
        page_open_close_browser.send_keys(Keys.ENTER)
        driver.implicitly_wait(20.0)
        driver.quit()
