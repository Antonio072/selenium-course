import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddRemoveElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.maximize_window()
        driver.find_element_by_link_text("Add/Remove Elements").click()

   
    def test_add_remove_elements(self):
        driver = self.driver

        elements_added = int(input("How many elements do you want to add? "))
        elements_removed = int(input("How many elements do you want to remove? "))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath("//button[contains(text(), 'Add Element')]")

        sleep(3)

        for i in range(elements_added):
            add_button.click()
            sleep(1)

        for i in range(elements_removed):
            try:
                delete_button = driver.find.element_by_xpath("//button[contains(text(), 'Delete')]")
                delete_button.click()
                sleep(1)
            except:
                print("No more elements to delete")
                break

        if total_elements >= 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print("There are no elements on screen")

        sleep(3)

        
        


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output="reportes", report_name= "Add Remove ELements"))
