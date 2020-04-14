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

class TestTestcase3profilereview():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testcase3profilereview(self):
    self.driver.get("http://127.0.0.1:8000/data/add/p/")
    self.driver.set_window_size(776, 741)
    dropdown = self.driver.find_element(By.ID, "id_blend_batch_id")
    dropdown.find_element(By.XPATH, "//option[. = 'Attikan Estate - 1']").click()
    element = self.driver.find_element(By.ID, "id_blend_batch_id")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "id_blend_batch_id")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "id_blend_batch_id")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "id_blend_batch_id").click()
    self.driver.find_element(By.ID, "id_user_id").click()
    self.driver.find_element(By.ID, "id_user_id").send_keys("897")
    dropdown = self.driver.find_element(By.ID, "id_acidic")
    dropdown.find_element(By.XPATH, "//option[. = '2-Recognisable']").click()
    element = self.driver.find_element(By.ID, "id_acidic")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "id_acidic")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "id_acidic")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "id_acidic").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(2)").click()
    dropdown = self.driver.find_element(By.ID, "id_sweet")
    dropdown.find_element(By.XPATH, "//option[. = '4-high']").click()
    element = self.driver.find_element(By.ID, "id_sweet")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "id_sweet")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "id_sweet")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "id_sweet").click()
    dropdown = self.driver.find_element(By.ID, "id_salty")
    dropdown.find_element(By.XPATH, "//option[. = '2-Recognisable']").click()
    element = self.driver.find_element(By.ID, "id_salty")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "id_salty")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "id_salty")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "id_salty").click()
    dropdown = self.driver.find_element(By.ID, "id_floral")
    dropdown.find_element(By.XPATH, "//option[. = '4-high']").click()
    element = self.driver.find_element(By.ID, "id_floral")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "id_floral")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "id_floral")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "id_floral").click()
    dropdown = self.driver.find_element(By.ID, "id_chocolaty")
    dropdown.find_element(By.XPATH, "//option[. = '4-high']").click()
    element = self.driver.find_element(By.ID, "id_chocolaty")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "id_chocolaty")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "id_chocolaty")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "id_chocolaty").click()
    dropdown = self.driver.find_element(By.ID, "id_nutty")
    dropdown.find_element(By.XPATH, "//option[. = '4-high']").click()
    element = self.driver.find_element(By.ID, "id_nutty")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "id_nutty")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "id_nutty")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "id_nutty").click()
    dropdown = self.driver.find_element(By.ID, "id_bitter")
    dropdown.find_element(By.XPATH, "//option[. = '4-high']").click()
    element = self.driver.find_element(By.ID, "id_bitter")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "id_bitter")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "id_bitter")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "id_bitter").click()
    dropdown = self.driver.find_element(By.ID, "id_savoury")
    dropdown.find_element(By.XPATH, "//option[. = '3-Moderate']").click()
    element = self.driver.find_element(By.ID, "id_savoury")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "id_savoury")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "id_savoury")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "id_savoury").click()
    dropdown = self.driver.find_element(By.ID, "id_spicy")
    dropdown.find_element(By.XPATH, "//option[. = '1-Little bit']").click()
    element = self.driver.find_element(By.ID, "id_spicy")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "id_spicy")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "id_spicy")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "id_spicy").click()
    dropdown = self.driver.find_element(By.ID, "id_berries")
    dropdown.find_element(By.XPATH, "//option[. = '4-high']").click()
    element = self.driver.find_element(By.ID, "id_berries")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "id_berries")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "id_berries")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "id_berries").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  