import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class SaveEscale(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver92')
        driver = self.driver
        driver.maximize_window()
        driver.get("http://sigmed.minedu.gob.pe/mapaeducativo/")
        sleep(5)
        
    def test_sort_tables(self):
        driver = self.driver        
        table_data = [[[] for k in range(25)] for k in range(25)]
        for i in range(25):
            departamento = driver.find_element_by_css_selector(f'#departamento > option:nth-child({i+1})')
            departamento.click()
            select_provincia = Select(self.driver.find_element_by_id('provincia'))
            for j in range(len(select_provincia.options)):
                provincia = driver.find_element_by_css_selector(f'#provincia > option:nth-child({j+1})')
                provincia.click()
                select_distrito = Select(self.driver.find_element_by_id('distrito'))
                b = len(select_distrito.options)
                for k in range(len(select_distrito.options)):
                    distrito = driver.find_element_by_css_selector(f'#distrito > option:nth-child({k+1})')
                    distrito.click()
                    driver.find_element_by_xpath('//*[@id="sel-ubigeo"]/div/div[4]/div[2]').click()
                    ubigeo = driver.find_element_by_id('txtcodubigeo')
                    ubigeo_codigo = ubigeo.get_attribute('value')
                    print(departamento.text+';'+provincia.text+';'+distrito.text+';'+ubigeo_codigo)
                    #table_data[i].append(str(departamento.text+';'+provincia.text+';'+distrito.text))                    
        #for i in range(5):
        #    header = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/table[1]/thead/tr/th[{i+1}]/span')
        #    table_data[i].append(header.text)
        #    
        #    for j in range(4):
        #      row_data = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/table[1]/tbody/tr[{j+1}]/td[{i+1}]')           
        #        table_data[i].append(row_data.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)