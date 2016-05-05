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

raceVal = ['"ASI"', '"BLK"', '"CAU"', '"HIS"']
genderVal = ['"F"', '"M"']
ageVal = ['"00"', '"01"', '"02"', '"03"', '"04"', '"05"', '"06"', '"07"', 
		'"08"', '"09"', '"10"', '"11"', '"12"', '"13"', '"14"', '"15"', 
		'"16"', '"17"', '"18"']

# Iterate all dropdown attribute combinations (i.e BLK FEMALE 12)

# Race iteration
for race in raceVal:
	# **There is an HTML misspelling which causes value to be spelled vaule**
	if race == "CAU":
		driver.find_element_by_xpath('//select[@name="Race"]/option[@vaule=' + race + ']').click()
	else:
		driver.find_element_by_xpath('//select[@name="Race"]/option[@value=' + race + ']').click()
	# Gender iteration
	for gender in genderVal:
		driver.find_element_by_xpath('//select[@name="Gender"]/option[@value=' + gender + ']').click()
		# Age iteration
		for age in ageVal:
			driver.find_element_by_xpath('//select[@name="Age"]/option[@value=' + age + ']').click()
			time.sleep(1)
			driver.find_element_by_xpath('//input[@value="Submit"]').click()
			htmlSource = driver.page_source
			soupObject = BeautifulSoup(htmlSource, 'html.parser')
			# Find all image links and download
			for item in soupObject.findAll('a'):
				rawLink = link.get('href')[:-3]
				landmark = rawLink.index("JPEG")
				linkURL = rawLink[landmark:]
				NAME = linkURL.rpartition('/')[0].rpartition('/')[2]
				UID = linkURL.rpartition('/')[2][:4]
				#print(link.get('href')[:-3])


			

