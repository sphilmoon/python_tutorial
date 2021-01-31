import requests
from bs4 import BeautifulSoup

limit = 5
url = f"https://www.indeed.com/jobs?q=Python&l=usa&limit={limit}&fromage=7"

def extract_pages():
	send = requests.get(url)
	soup = BeautifulSoup(send.text, "html.parser")

	pagination = soup.find("div", {"class": "pagination"})
	anchors = pagination.find_all('a')

	pages = []
	for anchor in anchors[:-1]:
		pages.append(int(anchor.string))

	max_page = (pages[-1])
	return max_page

def extract_jobs(html):
	title = html.find("h2", {"class": "title"}).find("a")["title"]
	company = html.find("span", {"class": "company"}).find("a")
	company_anchor = company.find("a")
	if company_anchor is not None:
		company = str(company_anchor.string)
	else:
		company = str(company.string)
	company = company.strip()
	location = html.find("span", {"class": "location"}).string
	job_id = html["data-jk"]
	return {"title": title, 
			"company": company, 
			"location": location, 
			"link": f"https://www.indeed.com/viewjob?jk={job_id}"
	}


def extract_last_jobs(last_page):
	jobs = []
	for page in range(last_page):
		print(f"Scrapping indeed pages {page}")
		send = requests.get(f"{url}&start={page*limit}")
		soup = BeautifulSoup(send.text, "html.parser")
		results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
		print(results)
	for result in results
		job = extract_jobs(result)
		jobs.append(job)
	return jobs	

# def extract_jobs():
# 	last_pages = extract_pages()
# 	jobs = extract_last_jobs(last_pages)
# 	return jobs
