from application import app
from flask import request, Response

@app.route("/", methods=["GET"])
def get_winner():
    number = request.json["number"]
    prize = request.json["prize"]
    
    if number == "1" and prize == "Iphone-12":
        return Response(" Congrats you won an Iphone-12", mimetype='text/plain')
    elif number == "2" and prize == "Ps5":
        return Response("Congrats you won a Ps5", mimetype='text/plain')
    elif number == "3" and prize == "Bitcoin":
        return Response("Congrats you some Bitcoin", mimetype='text/plain')
    else:
        return Response("Unfortunately you have not won anything!", mimetype='text/plain')
