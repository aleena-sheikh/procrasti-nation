import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")



@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        inc = request.form["income"] 
        current = request.form["age"]
        city = request.form["city"]
        retirement = request.form["retireage"]
        response = """ChatGPT is an artificial intelligence (AI) chatbot developed by OpenAI and released in November 2022. The name "ChatGPT" combines "Chat", referring to its chatbot functionality, and "GPT", which stands for Generative Pre-trained Transformer, a type of large language model (LLM).[2] ChatGPT is built upon OpenAI's foundational GPT models, specifically GPT-3.5 and GPT-4, and has been fine-tuned (an approach to transfer learning) for conversational applications using a combination of supervised and reinforcement learning techniques.\n

The prototype of ChatGPT was launched on November 30, 2022, and gained attention for its detailed and articulate responses spanning various domains of knowledge.[3] However, a notable drawback has been its tendency to confidently provide inaccurate information.[4] In 2023, after the release of ChatGPT, OpenAI's valuation was estimated at US$29 billion.[5] The introduction of ChatGPT has spurred competition in the field, leading to the accelerated development of Google's chatbot Bard, initially based on LaMDA and later on PaLM, as well as Meta AI's foundation model LLaMA, which serves as a basis for other chatbot creations.[6]\n

Initially, ChatGPT was based on GPT-3.5. However, a version using the newest OpenAI model, GPT-4, was released on March 14, 2023, and is currently available to paid subscribers of ChatGPT Plus on a limited basis."""

        #  response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt=generate_prompt(inc,current,city,retirement),
        #     temperature=0.6,
        #     max_tokens=40
        # )
        #return redirect(url_for("index",result=response )) #result=response.choices[0].text #response

    #result = request.args.get("result")
        #return response #render_template("index.html", result=result)
    if request.method == "GET": 
        response = """Some text here"""
    return response 
def generate_prompt(income,curr,city,ret):
    return f"""
    Request: Suggest in 3 time steps a financial plan for a 20 year old making 50,000 dollars annually in Phoenix such that they are able to retire by 60 years old
    Plan: 1.By 30 years old, maximize 401K. \n2.By 40 years old,diversify your assets and investments \n3. By 50 years old, have substantial networth in savings to be in good financial health
    Request: Suggest in 3 time steps a financial plan for a 30 year old making 100,000 dollars annually in Seattle such that they are able to retire by 60 years old
    Plan: 1.By 40 years old, targeted savings should be 7 times multiple of expected retirement savings \n2.By 50 years old,should have 15 times expected retirement spending \n3. By 60 years old, should have accrued 25 times expected retirement spending 
    Request: Suggest in 2 time steps a financial plan for a {curr} year old making {income} dollars annually in {city} such that they are able to retire by {ret} years old
    Plan:
"""