import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver

def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader, None) #Omitir primer dato (cabecera)
    
    for row in reader: #Lectura y adiciona de datos a rows
        rows.append(row)
    return rows
    
@ddt    
class SearchDDT(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver92')
        driver = self.driver
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
    
    @data(*get_data('testdata.csv')) #Decoradores instanciando valores
    @unpack #Desmpaquetar
    
    def test_seach_ddt(self, search_value, expected_count):
        driver = self.driver     
        search_field = driver.find_element_by_name('q')
        search_field.clear() #Borrar contenido de la barra de busqueda
        search_field.send_keys(search_value)
        search_field.submit()
        
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        expected_count = int(expected_count)
        
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', message)
        
        print(f'Found {len(products)} products')
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)