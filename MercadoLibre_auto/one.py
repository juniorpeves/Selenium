import unittest
from selenium import webdriver
from time import sleep
 
class TestingMercadoLibre(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'./chromedriver92')
		driver = self.driver
		driver.maximize_window()
		driver.get('https://www.mercadolibre.com')

	def test_search_PS4(self):
		driver = self.driver

		country = driver.find_element_by_id("CO")
		country.click()

		search_field = driver.find_element_by_name("as_word")
		search_field.click()
		search_field.clear()
		search_field.send_keys('playstation 4')
		search_field.submit()

		location = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section/dl[18]/dd[1]/a')
		driver.execute_script("arguments[0].click();", location)
		sleep(1)

		condition = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[2]/dl[16]/dd[1]/a')
		driver.execute_script("arguments[0].click();", condition)
		sleep(1)

		order_menu = driver.find_element_by_class_name("andes-dropdown__trigger")
		order_menu.click()

		higher_price = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div/div/ul/li[3]/a')
		driver.execute_script("arguments[0].click();", higher_price)
		sleep(1)

		articles = []
		prices = []

		for i in range(5):
			article_name = driver.find_element_by_css_selector(f'#root-app > div > div > section > ol > li:nth-child({i+1}) > div > div > div.ui-search-result__content-wrapper > div.ui-search-item__group.ui-search-item__group--title > a > h2').text
			articles.append(article_name)
			article_price = driver.find_element_by_css_selector(f'#root-app > div > div > section > ol > li:nth-child({i+1}) > div > div > div.ui-search-result__content-wrapper > div.ui-search-result__content-columns > div.ui-search-result__content-column.ui-search-result__content-column--left > div.ui-search-item__group.ui-search-item__group--price > a > div > div > span.price-tag.ui-search-price__part > span.price-tag-amount > span.price-tag-fraction').text
			prices.append(article_price)
		for x in range(len(articles)):
			print(prices[x]+' ...... '+articles[x])


	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()