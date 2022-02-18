from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#FirefoxProfile
options=Options()
options.profile = r"C:\Users\imani\AppData\Roaming\Mozilla\Firefox\Profiles\qic8u2xz.default"

#Start GeckoDriver
driver = webdriver.Firefox(options=options)

# # Website Link
driver.get('https://www.tradingview.com/crypto-screener/')

# # Maximize Window
driver.maximize_window()

# # Get element with tag name 'class_name'
links = driver.find_elements_by_class_name("tv-data-table__row .tv-screener__symbol")

pairs = [link.text for link in links]
print("Pairs", pairs)
driver.quit()