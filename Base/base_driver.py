import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    def pagescroll(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
                print("END OF PAGE")
            last_height = new_height
        time.sleep(4)

    def wait_for_presence_of_all_elements_located(self,locator_name, locator):
        wait = WebDriverWait(self.driver, 20)
        list_elements = wait.until(EC.presence_of_all_elements_located((locator_name, locator)))
        return list_elements

    def wait_element_to_be_clickable(self,locator_name, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((locator_name, locator)))
        return element
