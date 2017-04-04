from selenium import webdriver
import csv
chrome_path = r"C:\Users\Amulya\Desktop\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('http://www.officeholidays.com/countries/india/2016.php')
rows = driver.find_elements_by_css_selector('table.list-table tr')
rows = rows[1:]
writer = csv.writer(open('eventData2016.csv', 'w'))
for row in rows:
	cols = row.find_elements_by_css_selector('td')
	result = cols[0].text, cols[1].text, cols[2].text, cols[3].text
	writer.writerow(result)