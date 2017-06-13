from selenium import webdriver
import csv
chrome_path = r"C:\Users\Amulya\Desktop\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('http://www.mapsofindia.com/events/2016-holidays-calendar.html')
rows = driver.find_elements_by_css_selector('table.tableizer-table tr')
rows = rows[1:]
writer = csv.writer(open('scrapedDataGovtHolidays2016.csv', 'w'))
for row in rows:
	cols = row.find_elements_by_css_selector('td')
	result = cols[0].text, cols[1].text, cols[2].text, cols[3].text
	writer.writerow(result)