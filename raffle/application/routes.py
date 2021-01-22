from application import app
import requests
from flask import render_template

@app.route('/', methods= ['GET'])
def index():
    number_response = requests.get("http://SFIA2_number_backend:5001/number")
    prize_response = requests.get("http://SFIA2_prize_backend:5002/prize")
    winner_response = requests.post(
        "http://SFIA2_winner_backend:5003/winner",
        json=dict(number=number_response.text, prize=prize_response.text)
    )
    return render_template("index.html", prize=prize_response.text, number=number_response.text)

