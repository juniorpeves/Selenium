import unittest
from time import sleep
from selenium import webdriver

class Ordertable(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver92')
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Sortable Data Tables').click()
    
    def test_sort_tables(self):
        driver = self.driver
        
        table_data = [[] for i in range(5)]
        print(table_data)
        
        for i in range(5):
            header = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/table[1]/thead/tr/th[{i+1}]/span')
            table_data[i].append(header.text)
            for j in range(4):
                row_data = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/table[1]/tbody/tr[{j+1}]/td[{i+1}]')           
                table_data[i].append(row_data.text)
        print(table_data)        
        def Mostrar(a):
            print("La matriz es la siguiente:")
            for fila in a:
                for valor in fila:
                    print("\t", valor, end=" ")
                print()
        Mostrar(table_data)
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)