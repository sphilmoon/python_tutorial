from indeed2 import extract_pages, extract_last_jobs
from save import save_file

last_indeed_pages = extract_pages()
indeed_jobs = extract_last_jobs(last_indeed_pages)
jobs = indeed_jobs
save_file(jobs)


