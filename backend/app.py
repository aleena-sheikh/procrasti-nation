import os
from flask_cors import CORS
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
CORS(app)
openai.api_key = os.getenv("OPENAI_API_KEY")

#     Request: Suggest in 3 time steps a financial plan for a 20 year old making 50,000 dollars annually in Phoenix such that they are able to retire by 60 years old
#     Plan: 1.By 30 years old, maximize 401K. \n2.By 40 years old,diversify your assets and investments \n3. By 50 years old, have substantial networth in savings to be in good financial health
#     Request: Suggest in 3 time steps a financial plan for a 30 year old making 100,000 dollars annually in Seattle such that they are able to retire by 60 years old
#     Plan: 1.By 40 years old, targeted savings should be 7 times multiple of expected retirement savings \n2.By 50 years old,should have 15 times expected retirement spending \n3. By 60 years old, should have accrued 25 times expected retirement spending
def generate_prompt(income, curr, city, ret):
    return f"""

    Suggest in 5 time steps a financial plan for a {curr} year old making {income} dollars annually in {city} such that they are able to retire by {ret} years old
    
"""


@app.route("/", methods=("GET", "POST"))
def index(inc="70000", curr="10", city="Phoenix", ret="70"):
    if request.method == "GET" or request.method == "OPTIONS":
        response = {
            "hello": "Fill in your information to determine the path to FIRE(ETIRE)\n"
        }
    # response = """Fill in your information to determine the path to FIRE(ETIRE)\n"""
    if request.method == "POST":
        response = {
            "hello": openai.Completion.create(
                model="text-davinci-003",
                prompt=generate_prompt(inc, curr, city, ret),
                temperature=0.6,
                max_tokens=200,  # 2000,
            )
            .choices[0]
            .text
        }
    # generate_prompt(inc,curr,city,ret)}
    #         inc = request.form["income"]
    #         current = request.form["age"]
    #         city = request.form["city"]
    #         retirement = request.form["retireage"]

    #     response = openai.Completion.create(
    #         model="text-davinci-003",
    #         prompt=generate_prompt("30000", "25", "NYC", "70"),
    #         temperature=0.6,
    #         max_tokens=40,
    #     )

    return response  # response.choices[0].text


# return redirect(url_for("index",result=response )) #result=response.choices[0].text #response

# result = request.args.get("result")
# return response #render_template("index.html", result=result)
#     if request.method == "GET":
#         response = """Some text here"""
