import logging

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Pages.search_fligths_results_page import SearchFlightResult
from Utilities.utils import cls_utils


class Launchpage(BaseDriver):
    log = cls_utils.custlogger(loglevel=logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    Depart_from_field = "//input[@id='BE_flight_origin_city']"
    Arrival_to_Filed = "//label[@for='BE_flight_arrival_city']"
    going_to_result_list = "//div[@class='viewport']//div[1]//li"
    select_date_Field = "//input[@id='BE_flight_origin_date']"
    all_date_Field = "//div[@id='monthWrapper']//tbody//td[@class !='inActiveTD']"
    search_Button = "BE_flight_flsearch_btn"

    def getDepartFrom(self):
        return self.wait_element_to_be_clickable(By.XPATH,self.Depart_from_field)
    def getarrivalto(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.Arrival_to_Filed)

    def getgoingtolistresult(self):
        return self.driver.find_elements(By.XPATH, self.going_to_result_list)

    def getselectdate(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.select_date_Field)

    def getalldates(self):
        return self.wait_for_presence_of_all_elements_located(By.XPATH, self.all_date_Field)
    def getsearchbuton(self):
        return self.wait_element_to_be_clickable(By.ID, self.search_Button)
    def enterdepartformlocation(self,source):
        self.getDepartFrom().click()
        self.log.info("clicked depart form")
        self.getDepartFrom().send_keys(source)
        self.getDepartFrom().send_keys(Keys.ENTER)

    def enterarrivaltolocation(self,destination):
        self.getarrivalto().click()
        self.log.info("clicked going to")
        self.getarrivalto().send_keys(destination)
        self.log.debug("typed text into going to field sucessfully")
        search_destination = self.getgoingtolistresult()
        for result in search_destination:
            if "New York (JFK)" in result.text:  # my mistake result == 'destination':
                result.click()  # here it will work
                # result.send_keys(Keys.ENTER)
                break

    def dateofdeparture(self,departuredate):
        self.getselectdate().send_keys(Keys.RETURN)
        all_dates = self.getalldates()
        for dat in all_dates:
            if dat.get_attribute("data-date") == departuredate:
                dat.click()
                # dat.send_keys(Keys.ENTER) #here it wont work
                break

    def clicksearchfightsbutton(self):
        elem2 = self.getsearchbuton().send_keys(Keys.ENTER)

    def searchFlights(self,source, destination, departuredate):
        self.enterdepartformlocation(source)
        self.enterarrivaltolocation(destination)
        self.dateofdeparture(departuredate)
        self.clicksearchfightsbutton()
        search_flight_result = SearchFlightResult(self.driver)
        return search_flight_result

