import unittest
from selenium import webdriver
#Importacion para poder seleccionar 
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver92')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
    
    def test_select_language(self):
        exp_options = ['English','French','German']
        act_options = []
        #Crear variable para ubicar el dropdown
        select_language = Select(self.driver.find_element_by_id('select-language'))
        #Validar la cantidad de idiomas
        self.assertEqual(3, len(select_language.options))
        #Iterar la asignación de las opciones
        for option in select_language.options:
            act_options.append(option.text)
        
        #Validar la igual de las listas
        self.assertEqual(exp_options, act_options)
        #Verificando que la palabra English esta seleccionado
        self.assertEqual('English', select_language.first_selected_option.text)
        
        #Seleccionando German por su texto y validandolo con la URL
        select_language.select_by_visible_text('German')
        self.assertTrue('store=german' in self.driver.current_url)
        
        #Seleccionando English por su indice
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)
        
    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)