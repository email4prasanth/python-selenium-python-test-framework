import inspect
import logging

import softest

class cls_utils(softest.TestCase):
    def assert_list(self,list_allstops1,value):
        for stop in list_allstops1:
            print("the text is :" + stop.text)
            self.soft_assert(self.assertEqual,stop.text,value)
            if stop.text == value:
                print("assert pass ")
            else:
                print("test passed")
        self.assert_all()

    def custlogger(loglevel=logging.DEBUG):
        #Set class/Method name from where its called
        logger_name = inspect.stack()[1][3]
        # creat logger
        #logger = logging.getLogger(__name__)
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        # create console handle or file handler
        #ch = logging.StreamHandler()
        fh = logging.FileHandler("automation.log")
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt = '%d/%m/%Y %I:%M:%S %p')
        #fomatter1 = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
        # add formatter to ch
        #ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # add ch to logger
        #logger.addHandler(ch)
        logger.addHandler(fh)
        return logger