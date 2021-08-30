import unittest
from selenium import webdriver
from google_page import Google

class GoogleTest(unittest.TestCase):

    @classmethod#Decoradores para correr en una sola instancia del navegador
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'./chromedriver92')

    def test_search(self):
        google = Google(self.driver)
        google.open()
        google.search('Python')

        self.assertEqual('Python', google.keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()