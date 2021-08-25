import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):
    # Realiza todo lo necesario antes de empezar la prueba
    def setUp (self):
        # Abre el chrome
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        # maximiza la ventana, por el tamaño de vista
        driver.maximize_window()
        # esperamos 10 seg antes de realizar la siguiente accion
        driver.implicitly_wait(10)
        
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))
    
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))
    
    # Cerramos el navegador una vez terminadas las pruebas
    def tearDown (cls):
        cls.driver.quit()
        
    # Función de utilidad para indicar cuando un elemento esta presente
    # HOW el tipo de selector
    # WHAT el valor que tiene
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what) # Va buscar atravez de driver con los parametros indicados
        except NoSuchElementException as variable: # Asignando como variable
            return False
        return True    
