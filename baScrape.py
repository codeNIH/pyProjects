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
					destPATH = 'C:\\Users\\ipladmin\\Documents\\codeNIH\\pyProjects\\ASI\\'
				elif race == '"BLK"':
					destPATH = 'C:\\Users\\ipladmin\\Documents\\codeNIH\pyProjects\\BLK\\'
				elif race == '"CAU"':
					destPATH = 'C:\\Users\\ipladmin\\Documents\\codeNIH\\pyProjects\\CAU\\'
				elif race == '"HIS"':
					destPATH = 'C:\\Users\\ipladmin\\Documents\\codeNIH\\pyProjects\\HIS\\'

				metaID = "ID: " + UID + '\n'
				metaRace = "Race: " + str(metaData[1 + i*12]) + '\n'
				metaGender = "Gender: " + str(metaData[2 + i*12]) + '\n'
				metaChr = "Chronological Age: " + str(metaData[3 + i*12]) + '\n'
				metaDOB = "DOB: " + str(metaData[4 + i*12]) + '\n'
				metaExam = "Exam Date: " + str(metaData[5 + i*12]) + '\n'
				metaTanner = "Tanner: " + str(metaData[6 + i*12]) + '\n'
				metaHeight = "Height (cm): " + str(metaData[7 + i*12]) + '\n'
				metaWeight = "Weight (kg): " + str(metaData[8 + i*12]) + '\n'
				metaTrunk = "Trunk Height (cm): " + str(metaData[9 + i*12]) + '\n'
				metaRead1 = "Reading 1: " + str(metaData[10 + i*12]) + '\n'
				metaRead2 = "Reading 2: " + str(metaData[11 + i*12]) + '\n'
				

				urllib.urlretrieve(PATH+linkURL, destPATH + NAME + '_' + UID + '.jpg')
				textFile = open(destPATH + NAME + '_' + UID + '.txt', 'w')
				textFile.write(metaID + metaRace + metaGender + metaChr + metaDOB + metaExam + metaTanner + metaHeight + metaWeight + metaTrunk + metaRead1 + metaRead2)
				textFile.close()
				i += 1

			print '\n'


driver.quit()


			

