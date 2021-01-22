from application import app
from flask import request, Response
import random


@app.route("/prize", methods=["GET"])
def get_prize():
    prizes = ["Iphone-12", "Ps5", "Bitcoin"]
    return Response(str(random.choice(prizes)), mimetype='text/plain')
