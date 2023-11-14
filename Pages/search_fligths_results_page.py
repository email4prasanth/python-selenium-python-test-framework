import logging
import time
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Utilities.utils import cls_utils


class SearchFlightResult(BaseDriver):
    log = cls_utils.custlogger(loglevel=logging.WARNING)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    #Locators
    Filter_by_Nonstop = "//p[normalize-space()='0']"
    Filter_by_1stop = "//p[normalize-space()='1']"
    Filter_by_2stop = "//p[normalize-space()='2']"
    #SEARCH_FLIGHT_RESULTS ="dotted-borderbtm" #CLASSNAME
    SEARCH_FLIGHT_RESULTS ="// span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop(s)')]"

    def get_filter_by_0_stop(self):
        return self.driver.find_element(By.XPATH, self.Filter_by_Nonstop)
    def get_filter_by_1_stop(self):
        return self.driver.find_element(By.XPATH, self.Filter_by_1stop)
    def get_filter_by_2_stop(self):
        return self.driver.find_element(By.XPATH, self.Filter_by_2stop)

    def all_flight(self):
        return self.wait_for_presence_of_all_elements_located(By.XPATH,self.SEARCH_FLIGHT_RESULTS)
    def filter_flights_by_stop(self,by_stop):
        if by_stop == "Non Stop":
            self.get_filter_by_0_stop().click()
            self.log.warning("selected flights with no stop")
            time.sleep(4)

        elif by_stop == "1 Stop":
            self.get_filter_by_1_stop().click()
            self.logging.warning("selected flights with 1 stop")
            time.sleep(4)

        else:
            self.get_filter_by_2_stop().click()
            self.logging.warning("selected flights with 2 stop")
            time.sleep(4)
