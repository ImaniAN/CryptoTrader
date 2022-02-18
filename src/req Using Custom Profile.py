import re
import json
from http import cookies , cookielib
from selenium import webdriver
import urllib.request

driver = webdriver.Firefox()

cj = cookielib.MozillaCookieJar('A:\OneDrive\FGS\Endeavors\CryptoTrader\Cookies\cookies.txt')
cj.load(ignore_expires=True, ignore_discard=True)
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

print(cj)

cookies_list = driver.get_cookies()
cookies_dict = []
for cookie in cookies_list:
    cookies_dict.append([cookie['name'],cookie['value']])
cookies_dict = dict(cookies_dict)

"-profile", "/path/to/profile"

# Using Custom Profile

options=Options()
firefox_profile = FirefoxProfile()
# firefox_profile.set_preference("browser.link.open_newwindow", 3)
# firefox_profile.set_preference("browser.link.open_newwindow.disabled_in_fullscreen", False)
# firefox_profile.set_preference("services.sync.prefs.sync.browser.link.open_newwindow", False)
firefox_profile.path = r'C:\Users\imani\AppData\Local\Mozilla\Firefox\Profiles\na2ocyg2.Sel00'
#.set_preference("javascript.enabled", False)
#firefox_profile.set_preference("javascript.enabled", False)
options.profile = firefox_profile


# service_args
# options=Options()
# firefox_profile = FirefoxProfile()
# firefox_profile.set_preference("javascript.enabled", True)
# firefox_profile.profile_dir =  r'C:\Users\imani\AppData\Local\Mozilla\Firefox\Profiles\na2ocyg2.Sel00')
# options.profile = firefox_profile