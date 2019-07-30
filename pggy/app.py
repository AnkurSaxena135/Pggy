from flask import Flask, request, render_template, url_for, send_from_directory
from flask_restful import Resource, Api, reqparse
import random

app = Flask(__name__, static_folder='static')
api = Api(app)

store = {}

class Transaction(Resource):
    def put(self, tr_id):
        details = request.form["details"]
        store[tr_id] = {"id": tr_id, "details": details}
        return store[tr_id]
    
    def get(self, tr_id):
        if tr_id in store:
            print("Match found!")
            return {'result': store[tr_id]}
        else: 
            print("No match found!")
            return {'result': None}

class Transactions(Resource):
    def get(self):
        return {"result": store}
    
    def post(self):
        details = request.form
        print(details)
        tr_id = random.randint(100,200)
        store[tr_id] = {"id": tr_id, "details": details}
        return store[tr_id]

@app.route("/")
def login():    
    return render_template("index.html")

api.add_resource(Transaction, '/transaction/<string:tr_id>')
api.add_resource(Transactions, '/transactions')

if __name__ == '__main__':
    app.run(debug=True)