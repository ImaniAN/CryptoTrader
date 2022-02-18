from selenium import webdriver
from selenium_cookies import CookieHandler
dummy_driver = webdriver.Firefox()
#   The second argument is the page to go to when saving/loading cookies.
#   In some cases this is necessary for the loading and saving of cookies
#   to actually work. If you don't have this issue, you can just set it to None.
cookie_handler = CookieHandler(dummy_driver,"https://github.com/adamhb123/selenium_cookies",
                               overwrite=False, filename="cooks", wait_time=5)
#   save_cookies() saves the site cookies to the specified file
saved_cookies = cookie_handler.save_cookies()
#   load_cookies() loads the saved cookies from the given file (or from the most recently saved one)
loaded_cookies = cookie_handler.load_cookies()
print("Saved cookies == loaded cookies == cookie_handler.loaded_cookies: " + str(
        saved_cookies == loaded_cookies == cookie_handler.loaded_cookies))