from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import csv
import time

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("(insert chromedriver path)")
browser.get(url)
print("getting " + url + " please wait")
time.sleep(5)
print("done getting site")
header = ['name', 'distance', 'mass', 'radius']
planet_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    tbody = soup.select("table.jquery-tablesorter tbody")[1]
    for ul in tbody.find_all("tr"):
        l = ul.find_all("td")
        indexes = [l[0], l[5], l[7], l[8]]
        template = []
        for index, e in enumerate(indexes):
            try:
                template.append(e.find_all("a")[0].contents[-1].replace("\n", ""))
            except:
                try:
                    template.append(e.contents[0].replace("\n", ""))
                except:
                    template.append("n/a")

        print(template)
        planet_data.append(template)
    
    print("done...")
    print("fully done")
    with open('field_brown_dwarfs.csv', "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header)
        csv_writer.writerows(planet_data)
        print("written file!")
    
                


scrape()