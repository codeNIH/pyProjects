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

raceVal = ['"BLK"']
genderVal = ['"F"']
#ageVal = ['"00"', '"01"', '"02"', '"03"', '"04"']
ageVal = ['"00"']

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
			#time.sleep(1)
			driver.find_element_by_xpath('//input[@value="Submit"]').click()
			htmlSource = driver.page_source
			soupObject = BeautifulSoup(htmlSource, 'html.parser')

			metaData = []

			for row in soupObject.find_all("td"):
				item = row.getText()
				metaData.append(item)
			
			i = 0
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

				metaID = UID
				metaRace = "Race: " + str(metaData[1 + i*12])
				metaGender = "Gender: " + str(metaData[2 + i*12])
				metChr = "Chronological Age: " + str(metaData[3 + i*12])
				metaDOB = "DOB: " + str(metaData[4 + i*12])
				metaExam = "Exam Date: " + str(metaData[5 + i*12])
				metaTanner = "Tanner: " + str(metaData[6 + i*12])
				metaHeight = "Height (cm): " + str(metaData[7 + i*12])
				metaWeight = "Weight (kg): " + str(metaData[8 + i*12])
				metaTrunk = "Trunk Height (cm): " + str(metaData[9 + i*12])
				metaRead1 = "Reading 1: " + str(metaData[10 + i*12])
				metaRead2 = "Reading 2: " + str(metaData[11 + i*12])
				

				#urllib.urlretrieve(PATH+linkURL, destPATH+ NAME + '_' + UID + '.jpg')
				i += 1

			print '\n'
			# for item in metaData:
			# 	print item


driver.quit()


			

