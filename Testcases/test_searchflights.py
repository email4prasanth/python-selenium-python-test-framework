#Tried 3 hrs i think there is an upgrade in selenium 4
import logging

import pytest
from Pages.yata_launch_page import Launchpage
from Utilities.utils import cls_utils
import softest
from ddt import ddt, data, unpack



@pytest.mark.usefixtures("setup")
@ddt
class Testsearchflight(softest.TestCase):
    log = cls_utils.custlogger()
    @pytest.fixture(autouse=True)
    def class_set(self):
        self.lp = Launchpage(self.driver)
        self.obj_util = cls_utils()

    @data(("Bangalore","New York (JFK)", "30/12/2023","Non Stop"),("BOM","MAA","26/12/2023","Non Stop"))
    @unpack
    def test_flightsearch_non_stop(self,source1,destination1,depdate1,num_stop):
        searchflighresult = self.lp.searchFlights(source1,destination1,depdate1)
        self.lp.pagescroll()
        searchflighresult.filter_flights_by_stop(num_stop)
        allstops1 = searchflighresult.all_flight()
        self.log.warning(len(allstops1))
        self.obj_util.assert_list(allstops1,num_stop)


    # def test_flightsearch_1_stop(self):
    #     #searchflighresult = self.lp.searchFlights(source1,destination1,depdate1)
    #     searchflighresult = self.lp.searchFlights("Bangalore","New York (JFK)", "30/12/2023")
    #     self.lp.pagescroll()
    #     searchflighresult.filter_flights_by_stop("1 Stop")
    #     allstops1 = searchflighresult.all_flight()
    #     self.obj_util.assert_list(allstops1,"1 Stop")





