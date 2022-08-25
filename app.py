import os
import openai
import authapi
from flask import Flask, render_template, request, flash
app = Flask(__name__, static_url_path='/static')
app.secret_key = "RoamingGiraffe12"

@app.route("/")
def index():
    flash("Create a one page information website with AI")
    return render_template("index.html")
@app.route("/generate", methods=["POST", "GET"])    
def generate():
    openai.organization = "org-SnuqljBeSr8VdBfdkdiUOGb8"
    openai.api_key = authapi.apikey
    openai.Model.list()
    businessName=request.form['bizName']
    keywords=request.form['keywords']
    businessType=request.form['bizType']
    fullName=request.form['ownerName']
    completion = openai.Completion.create(engine="text-curie-001", prompt=f"write a long description with a call to action about a {businessType}. Write it using the keywords {keywords}. the name of the business is {businessName} and it's owned by {fullName}", max_tokens=2)
    flash(completion['choices'][0]['text'])
    return render_template("index.html")


openai.organization = "org-SnuqljBeSr8VdBfdkdiUOGb8"
openai.api_key = authapi.apikey
openai.Model.list()
# from newspaper import Article
# from textblob import TextBlob
# from requests import request, Request
# url='https://www.reddit.com/r/webdev/comments/2e0r3y/why_do_we_hate_godaddy/'
# article=Article(url)
# article.download()
# article.parse()
# article.nlp()
# text=article.summary
# blob=TextBlob(text)
# sentiment=blob.sentiment.polarity
business="photography business in florida"
keywords="Miami, portrait shoots, wedding shoots."
# completion = openai.Completion.create(engine="text-curie-001", prompt=f"write a long description with a call to action about a {businessName} . Write it using the keywords {keywords} the name of the business is Miami Profile and it's owned by Gonzalo Casas", max_tokens=5)
# print(completion['choices'][0]['text'])

