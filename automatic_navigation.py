import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep

class NavigationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
        driver = self.driver
        driver.get("http://www.google.com/")
        driver.maximize_window()

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output="reportes", report_name= "Compare Products"))
