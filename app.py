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
    if request.method == 'POST':
        tokenAmount=300
        tokenTitles=30
        openai.organization = "org-SnuqljBeSr8VdBfdkdiUOGb8"
        openai.api_key = authapi.apikey
        openai.Model.list()
        businessName=request.form['bizName']
        keywords=request.form['keywords']
        businessType=request.form['bizType']
        fullName=request.form['ownerName']
        location=request.form['location']
        service1=request.form['service1']
        service2=request.form['service2']
        service3=request.form['service3']
        heading1=openai.Completion.create(engine="text-curie-001", prompt=f"generate a title for {businessType} in {location}", max_tokens=tokenTitles)
        heading2=openai.Completion.create(engine="text-curie-001", prompt=f"generate a title for an about section for {businessName} that does {businessType} in {location}", max_tokens=tokenTitles)
        heading3=openai.Completion.create(engine="text-curie-001", prompt=f"generate a title for service section for {businessType} in {location}", max_tokens=tokenTitles)
        heading4=openai.Completion.create(engine="text-curie-001", prompt=f"generate a title for why you should hire {businessName} that does {businessType} in {location}", max_tokens=tokenTitles)

        heading_1=heading1['choices'][0]['text']
        heading_2=heading2['choices'][0]['text']
        heading_3=heading3['choices'][0]['text']
        heading_4=heading4['choices'][0]['text']
        bizPrompt=f"""Generate several paragraphs about a business that works with {businessType}. Write it using the keywords {keywords}. the name of the business is {businessName} and it's owned by {fullName}. it's located in {location}
        rules:
    - no phone numbers
    - don't include personal data like proper nouns, real places, etc.
    - formal wording
    -include persuasive wording  """
        about=f"""Generate an about section about a business that works with {businessType}. the name of the business is {businessName} and it's owned by {fullName}. it's located in {location}
        rules:
    - no phone numbers
    - don't include personal data like proper nouns, real places, etc.
    - formal wording
    -include persuasive wording  """

        service=f"""Write 1 paragraph for each of this service in {location}:
        -{service1}
        -{service2}
        -{service3} 
        rules:
    - no phone numbers
    - don't include personal data like proper nouns, real places, etc.
    - formal wording
    -include persuasive wording  """

        hireUs=f"""write about why you should hire my {businessType} business. the name of the business is {businessName}. it's located in {location}
        rules:
    - no phone numbers
    - don't include personal data like proper nouns, real places, etc.
    - formal wording
    -include persuasive wording  """
        generalRes = openai.Completion.create(engine="text-curie-001", prompt=bizPrompt, max_tokens=tokenAmount)
        aboutRes= openai.Completion.create(engine="text-curie-001", prompt=about, max_tokens=tokenAmount)
        serviceRes= openai.Completion.create(engine="text-curie-001", prompt=service, max_tokens=tokenAmount*2)
        hireUsRes= openai.Completion.create(engine="text-curie-001", prompt=hireUs, max_tokens=tokenAmount)
        # flash(heading1['choices'][0]['text'])
        # flash(general['choices'][0]['text'])
        # flash(about['choices'][0]['text'])
        # flash(service['choices'][0]['text'])
        # flash(hireUs['choices'][0]['text'])
        General=generalRes['choices'][0]['text']
        About=aboutRes['choices'][0]['text']
        Service=serviceRes['choices'][0]['text']
        HireUs=hireUsRes['choices'][0]['text']
    return render_template('index.html', **locals())


# openai.organization = "org-SnuqljBeSr8VdBfdkdiUOGb8"
# openai.api_key = authapi.apikey
# openai.Model.list()
# bizPrompt=f"""Generate several paragraphs about a business that works with photography. Write it using the keywords photoshoot. the name of the business is miami profile and it's owned by gonzalo casas. it's located in Miami, Florida
#      rules:
# - no phone numbers
# - don't include personal data like proper nouns, real places, etc.
# - formal wording
# -include persuasive wording  """
# completion = openai.Completion.create(engine="text-curie-001", prompt=bizPrompt, max_tokens=600)
# print(completion['choices'][0]['text'])



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
if __name__ == "__main__":
    app.run(debug=True)
