import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class Typos(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver92')
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Typos').click()
    
    def test_dynamic_controls(self):
        driver = self.driver
        #Tomando el texto del parrafo
        paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
        text_to_check = paragraph_to_check.text
        print(text_to_check) #Comprobando que obtuvo el texto
        
        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."
        #Mientras no encuentre el parrafo correcto, refresca
        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
            text_to_check = paragraph_to_check.text
            tries += 1
            driver.refresh()
        #Mientras no sigue siendo falso, se hará la condicional    
        while not found:
            if text_to_check == correct_text:
                driver.refresh()
                found = True
        #Si found ya cambia a true, la prueba continua..
        self.assertEqual(found, True)
        print(f"It took {tries} tries to find the typo")   
                    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)