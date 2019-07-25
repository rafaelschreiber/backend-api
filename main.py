from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from plugins.randomemail.randomemail import *

app = Flask(__name__)
api = Api(app)

api.add_resource(RandomEmail, "/randomemail")

if __name__ == "__main__":
    app.run()
