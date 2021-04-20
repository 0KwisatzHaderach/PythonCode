#Script for using the CRA calculator instead of clicking in a browser

#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

wd = webdriver.Firefox()

wd.get('https://www.canada.ca/en/revenue-agency/services/e-services/e-services-businesses/payroll-deductions-online-calculator.html')


# %%
