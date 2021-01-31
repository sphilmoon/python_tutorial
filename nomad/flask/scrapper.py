import requests
from bs4 import BeautifulSoup

def get_last_page(url):
	pages = []
	send = requests.get(url)
	soup = BeautifulSoup(send.text, "html.parser")
	pagination = soup.find("div", {"class": "pagination"})
	last_page = pages[-2].get_text(strip=True)
	return int(last_page)


def extract_jobs(html):
	title = html.find("h2", {"class": "title"}).find("a")["title"]
	company, location = html.find("h3").find_all("span", recursive=False)
	company = company.get_text(strip=True)
	location = location.get_text(strip=True).strip("-").strip(" \r").strip("\n")
	job_id = html["data-jobid"]
	return {"title": title, 
			"company": company, 
			"location": location, 
			"link": f"https://www.indeed.com/viewjob?jk={job_id}"
	}


def extract_last_jobs(last_page, url):
	jobs = []
	for page in range(last_page):
		print(f"Scrapping indeed job posts... {page}")
		send = requests.get(f"{url}&pg={page+1}")
		for result in results:
			job = extract_jobs(results)
			jobs.append(job)
		return jobs


def get_jobs(word):
	url = f"https://www.indeed.com/jobs?q={word}&l=usa&fromage=7"
	last_page = get_last_page(url)
	jobs = extract_last_jobs(last_page, url)
	return jobs	



