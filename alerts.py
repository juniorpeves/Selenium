import unittest
from selenium import webdriver

class CompareProduct(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver92')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
    
    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q') #Ubicando por name el campo de busqueda
        search_field.clear() #Borrando campo
        search_field.send_keys('tee') 
        search_field.submit() #Enviando la busqueda de busqueda
        
        driver.find_element_by_class_name('link-compare').click() #Agregando camisa para comprarar
        driver.find_element_by_link_text('Clear All').click() #Click
        
        alert = driver.switch_to_alert() #Creando variable y cambiando el foco (Atención)
        alert_text = alert.text #Extrayendo el texto
        self.assertEqual('Are you sure you would like to remove all products from your comparison?',alert_text)
        alert.accept()
        
    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)