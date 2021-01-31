#!/usr/local/bin python
# goal is to get indeed.html and extract the information.

# use 'requests' to send the html to my script.
# use 'beautiful soup' to extract information from html.

import requests
from bs4 import BeautifulSoup

limit = 5
url = f"https://www.indeed.com/jobs?q=Python&l=usa&limit={limit}&fromage=7"

def extract_indeed_pages():
# requesting html to my script.
	results = requests.get(url)

# extracting the whole html from text file. 
	soup = BeautifulSoup(results.text, "html.parser")

# from here, using the 'soup' to extract the "page" information from indeed source code.
	pagination = soup.find("div", {"class": "pagination"})

# find all the anchors/links from pagination.
	links = pagination.find_all('a')

# selecting only the "spans" from the links.
	spans = [] # create "spans" list.
	for link in links[:-1]:
		spans.append(int(link.find("span").string))
		# OR spans.append(int(link.string))

# print the "span" output. 
# get rid of the last row.
	max_spans = spans[-1] 
	return max_spans


def extract_indeed_jobs(last_pages):
	for page in range(last_pages):
		result = requests.get(f"{url}&start={page*limit}")
		

print(result)
