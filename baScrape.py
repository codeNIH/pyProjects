from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

'''Objective: 
1. Iterate though all IPIlab Race, Gender, and Age options
2. Download image
3. Create "linked" meta data text file with all attached data
'''

# Open webpage in Firefox browser
driver = webdriver.Firefox()
driver.get("http://www.ipilab.org/BAAweb/")

# Dropdown menu attributes, according to source code
raceID = ["ASI", "BLK", "CAU", "HIS"]
genderID = ["F", "M"]
ageID = ["00", "01", "02", "03", "04", "05", "06", "07", 
		"08", "09", "10", "11", "12", "13", "14", "15", 
		"16", "17", "18"]

for race in raceID:
	if race == "CAU":
		driver.find_element_by_xpath('//select[@name=' + race + ']' + '/option[@value=')
	driver.find_element_by_xpath('//select[@name=' + race + ']' + '/option[@value=')

