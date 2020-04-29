"""
@author: Juraj Holub (xholub40)
@project ITS project
@date April 2020
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

def setup(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.wait = WebDriverWait(context.driver, 5)

def teardown(context):
    context.driver.quit()

