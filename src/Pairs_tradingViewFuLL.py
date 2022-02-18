# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTradingView():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tradingView(self):
    self.driver.get("https://www.tradingview.com/crypto-screener/")
    self.driver.set_window_size(1382, 744)
    self.driver.execute_script("window.scrollTo(0,0)")
    self.vars["Pairs"] = self.driver.find_element(By.CSS_SELECTOR, ".tv-data-table__row .tv-screener__symbol").text
    self.driver.close()
  
