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
    
    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input('How many element will you add?')) #Input cuantos agregar
        elements_removed = int(input('How many elements will you remove?')) #Input cuantos eliminar
        total_elements = elements_added - elements_removed
        
        add_buttonn = driver.find_element_by_xpath('/html/body/div[2]/div/div/button') #Seleccionando el botón add
        sleep(3)
        
        for i in range(elements_added):
            add_buttonn.click() #agregar elemento    
        for i in range(elements_removed):
            try: #Try para eliminar elemento
                delete_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/button[1]')
                delete_button.click()
            except: #Except para no eliminar mas de los existentes
                print("You're trying to delete more elements the existent")                
        if total_elements > 0: #Condicional para mostrar cuantos elementos quedan
            print(f"There are {total_elements} elements on screen")
        else:
            print("There 0 are elements on screen")
        
        sleep(3) #Pausa
            
    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)