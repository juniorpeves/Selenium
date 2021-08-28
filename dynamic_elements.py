import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver92')
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Disappearing Elements').click()
    
    def test_name_elements(self):
        driver = self.driver
        
        options = [] #creando lista vacia
        menu = 5
        tries = 1
        
        while len(options) < 5: #medir la longitud de opciones
            options.clear()
            
            for i in range(menu): #Iterando atraves de menu
                try:
                    #Guardar el elemento que se muestra en pantalla
                    option_name = driver.find_element_by_xpath(f"/html/body/div[2]/div/div/ul/li[{i+1}]/a")
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option numbre {i+1} is NOT FOUND") #No encontrado
                    tries +=1
                    driver.refresh()
                    
        print(f"Finished in {tries} tries")                           
            
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)