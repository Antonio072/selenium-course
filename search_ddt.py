import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from ddt import ddt, data, unpack

@ddt
class SearchDDT(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")

    @data(('dress', 6), ('music', 5))
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()
        
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        print(f'Found {len(products)} products for {search_value}')

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output="reportes", report_name= "SearchDDT"))
