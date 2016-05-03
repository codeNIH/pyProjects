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
raceName = "Race"
genderName = "Gender"
ageName = "Age"

raceVal = ["ASI", "BLK", "CAU", "HIS"]
genderVal = ["F", "M"]
ageVal = ["00", "01", "02", "03", "04", "05", "06", "07", 
		"08", "09", "10", "11", "12", "13", "14", "15", 
		"16", "17", "18"]

for race in raceVal:
	if race == "CAU":
		driver.find_element_by_xpath('//select[@name=' + raceName + ']/option[@vaule=' + raceVal + ']').click()
	else:
		driver.find_element_by_xpath('//select[@name=' + raceName + ']/option[@value=' + raceVal + ']').click()
	for gender in genderVal:
		driver.find_element_by_xpath('//select[@name=' + genderName + ']/option[@value=' + genderVal + ']').click()
		for age in ageVal:
			driver.find_element_by_xpath('//select[@name=' + ageName + ']/option[@value=' + ageVal + ']').click()
			

