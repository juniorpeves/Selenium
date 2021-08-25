import unittest
from selenium import webdriver

class HomePageTest (unittest.TestCase):
    # Realiza todo lo necesario antes de empezar la prueba
    @classmethod
    def setUp (cls):
        # Abre el chrome
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        # maximiza la ventana, por el tamaño de vista
        driver.maximize_window()
        # esperamos 10 seg antes de realizar la siguiente accion
        driver.implicitly_wait(10)
    # Busqueda por ID
    def test_search_text_field_id (self):
        search_field = self.driver.find_element_by_id("search")
    # Busqueda por name
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")
    # Busqueda por class
    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")
    # Busqueda por button
    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")
    # Busqueda por lista (ul li) de imagenes con condicional de cantidad
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))
    # Busqueda por XPatch, click derecho luego de Inspeccionar
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')
    # Busqueda por selector de css
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")
    # Cerramos el navegador una vez terminadas las pruebas
    @classmethod
    def tearDown (cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)