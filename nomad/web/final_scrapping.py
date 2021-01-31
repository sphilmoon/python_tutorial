from indeed2 import extract_pages, extract_last_jobs

last_indeed_pages = extract_pages()
#print(last_indeed_pages)

# extract_last_jobs(last_indeed_pages)

indeed_jobs = extract_last_jobs(last_indeed_pages)
print(indeed_jobs)

#print(extract_last_jobs)


#last_indeed_pages = extract_max_indeed_jobs()
#print(last_indeed_pages)

#extract_indeed_jobs(max_indeed_pages)


#last_indeed_pages = extract_indeed_jobs()