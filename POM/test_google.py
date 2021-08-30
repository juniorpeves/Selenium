import unittest
from selenium import webdriver
from google_page import Google
from time import sleep

class GoogleTest(unittest.TestCase):

    @classmethod#Decoradores para correr en una sola instancia del navegador
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'./chromedriver92')

    def test_search(self):
        google = Google(self.driver)
        google.open()               #Llamada a el metodo open de la clase google
        google.search('Python')     #Llamada a el metodo search de la clase google 

        self.assertEqual('Python', google.keyword) #Validando los valores del input y search
        sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()