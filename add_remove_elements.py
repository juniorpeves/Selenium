import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver92')
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Add/Remove Elements').click()

            
    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)