from application import app
from flask import request, Response
import random

#@app.route("/prize", method=["GET"])
#def get_prize():
#    prizes = ["PS5", "IPHONE12", "BITCOIN"]
#   return Response(str(random.choice(prizes)), mimetype='text/plain')

@app.route("/number", methods=["GET"])
def get_number():
    numbers = ["1", "2", "3"]
    return Response(str(random.choice(numbers)), mimetype='text/plain')
