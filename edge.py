from msedge.selenium_tools import EdgeOptions, Edge

options = EdgeOptions()
options.use_chromium = True
options.binary_location = r"/usr/bin/microsoft-edge-dev"
options.set_capability("platform", "LINUX")

webdriver_path = r"./msedgedriver"

browser = Edge(options=options, executable_path=webdriver_path)
browser.get("https://www.google.com")
acceder = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[2]/a')
acceder.click()
usuario = browser.find_element_by_id("identifierId")
usuario.send_keys('juniorpeves')
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
browser.get("https://web.whatsapp.com/send?phone=51931847494")