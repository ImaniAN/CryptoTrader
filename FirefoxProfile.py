from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium_cookies import CookieHandler


#FirefoxProfile
options=Options()
options.arguments("-profile")
#options.arguments = ["-profile", r"C:\Users\imani\AppData\Roaming\Mozilla\Firefox\Profiles\rg8axzck.default-release"]
#.profile = r"C:\Users\imani\AppData\Roaming\Mozilla\Firefox\Profiles\rg8axzck.default-release"

#Start GeckoDriver
dummy_driver = webdriver.Firefox(options = options)
#   The second argument is the page to go to when saving/loading cookies.
#   In some cases this is necessary for the loading and saving of cookies
#   to actually work. If you don't have this issue, you can just set it to None.
cookie_handler = CookieHandler(dummy_driver,"https://www.tradingview.com/crypto-screener/",
                               overwrite=False, filename="cooks", wait_time=5)

# # Get element with tag name 'class_name'
links = dummy_driver.find_elements_by_class_name("tv-data-table__row .tv-screener__symbol")

pairs = [link.text for link in links]
print("Pairs + ,pairs")
dummy_driver.quit()