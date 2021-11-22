import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output="reportes", report_name= "POM Google"))
