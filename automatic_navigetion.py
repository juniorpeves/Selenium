import unittest
from selenium import webdriver
from time import sleep #NO RECOMENDADO

class NavigationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver92')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://google.com/')
    
    def test_browser_navigetion(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q') #Ubicar la barra de busqueda
        search_field.clear() #Borrar los datos en la barra de busqueda
        search_field.send_keys('platzi') #Ingresar la palabra
        search_field.submit() # Hacer la busqueda
        
        driver.back() #Retroceder pagina
        driver.forward() #Avanzar pagina
        driver.refresh() #Refrescar pagina
        sleep(3)
        
    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)