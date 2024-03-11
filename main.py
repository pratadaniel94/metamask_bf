from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scrapping:
    def __init__(self, driver):
        self.driver = driver

    def __get_componets_ids(self)-> dict:
        return {}

    def get_url(self):
        return self.url

    def navigate(self, url=None):
        self.driver.get(url or self.url)

    def run(self):

        EXTENSION_PATH = os.getenv("EXTENSION_PATH")
        EXTENSION_ID = os.getenv('EXTENSION_ID')


        opt = webdriver.ChromeOptions()
        opt.add_extension(EXTENSION_PATH)
        driver = webdriver.Chrome(options=opt)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))


        # driver.switch_to.window(driver.window_handles[1])
        # self.driver.find_element(By.ID, "formBody_txtUser")
        # checkbox = driver.find_element(by=By.XPATH, value="onboarding__terms-checkbox")

        # Locate the checkbox element

        checkbox = driver.find_element(By.ID,"onboarding__terms-checkbox")


    def close(self):
        self.driver.close()
