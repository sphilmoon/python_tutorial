from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_file

app = Flask("super_scrapper")

db = {}

# use the decorator to execute functions below. 
@app.route("/")
def home():
	return render_template("template.html")

# dynamic urls
@app.route("/report")
def report():
	word = request.args.get('word')
	if word:
		word = word.lower()
		hiring = db.get(word)
		if hiring:
			jobs = hiring
		else:
			jobs = get_jobs(word)
			db[word] = jobs
	else:
		return redirect("/")
	return render_template("report.html", searching=word, quant=len(jobs), jobs = jobs) 

@app.route("/export")
def export():
	try:
		word = word.lower()
		word = request.args.get('word')
		if not word:
			raise Exception() 
		jobs = db.get(word)
		if not jobs:
			raise Exception()
		save_file(jobs)
		return send_file("jobs.csv")
	except:
		return redirect("/")


app.run()

