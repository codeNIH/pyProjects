from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import urllib

'''Objective: 
1. Iterate though all IPIlab Race, Gender, and Age options
2. Download image
3. Create "linked" meta data text file with all attached data
'''

PATH = "http://www.ipilab.org/BAAweb/"

# Open webpage in Firefox browser
driver = webdriver.Firefox()
driver.get(PATH)

# Dropdown menu attributes, according to source code
raceName = "Race"
genderName = "Gender"
ageName = "Age"

# raceVal = ['"ASI"', '"BLK"', '"CAU"', '"HIS"']
# genderVal = ['"F"', '"M"']
# ageVal = ['"00"', '"01"', '"02"', '"03"', '"04"', '"05"', '"06"', '"07"', 
# 		'"08"', '"09"', '"10"', '"11"', '"12"', '"13"', '"14"', '"15"', 
# 		'"16"', '"17"', '"18"']

raceVal = ['"ASI"', '"BLK"']
genderVal = ['"F"', '"M"']
ageVal = ['"00"', '"01"', '"02"', '"03"', '"04"']

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
			for link in soupObject.findAll('a'):
				rawLink = link.get('href')[:-3]
				landmark = rawLink.index("JPEG")
				linkURL = rawLink[landmark:]
				NAME = linkURL.rpartition('/')[0].rpartition('/')[2]
				UID = linkURL.rpartition('/')[2][:4]

				if race == '"ASI"':
					destPATH = '/Users/alexgeorge/Dropbox/Python/codeNIH/Images/ASI/'
				elif race == '"BLK"':
					destPATH = '/Users/alexgeorge/Dropbox/Python/codeNIH/Images/BLK/'
				elif race == '"CAU"':
					destPATH = '/Users/alexgeorge/Dropbox/Python/codeNIH/Images/CAU/'
				elif race == '"HIS"':
					destPATH = '/Users/alexgeorge/Dropbox/Python/codeNIH/Images/HIS/'

				urllib.urlretrieve(PATH+linkURL, destPATH+ NAME + '_' + UID + '.jpg')

				print NAME+UID
				#print(link.get('href')[:-3])


			

