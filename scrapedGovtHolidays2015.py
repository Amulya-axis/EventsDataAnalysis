from selenium import webdriver
import csv
chrome_path = r"C:\Users\Amulya\Desktop\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('http://portalseven.com/calendar/Holidays_India.jsp?year=2015')
rows = driver.find_elements_by_css_selector('table.table.table-striped.table-bordered.table-condensed.table-hover tr')
rows = rows[2:]
writer = csv.writer(open('scrapedDataGovtHolidays2015.csv', 'w'))
for row in rows:
	cols = row.find_elements_by_css_selector('td')
	result = cols[0].text, cols[1].text, cols[2].text
	writer.writerow(result)

