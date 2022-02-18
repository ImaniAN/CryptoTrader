from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

#FirefoxProfile
options=Options()
#options.arguments = ["-profile", r"C:\Users\imani\AppData\Roaming\Mozilla\Firefox\Profiles\rg8axzck.default-release"]
options.arguments["-profile"])
#Start GeckoDriver
driver = webdriver.Firefox(options=options)
#driver = webdriver.Firefox()


# # Website Link
driver.get('https://www.tradingview.com/crypto-screener/')

# # Maximize Window  -connect-existing --marionette-port 8080
# driver.maximize_window()

# # Get element with tag name 'class_name'
# links = driver.find_elements_by_class_name("tv-data-table__row .tv-screener__symbol")

# pairs = [link.text for link in links]
print("Pairs + ,pairs")
driver.quit()