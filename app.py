from flask import Flask, request, jsonify, Response
import json
from datetime import datetime
import database.firestore as firestore
import database.model as model
Model = model.Model()
app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
  users = Model.getAllUsers()
  print(users)
  return Response(status=200)

@app.route('/users', methods=['POST'])
def post_users():
  newUser = {}
  requiredFields = ['firstName', 'lastName', 'calendarType', 'calendarUrl', 'subscriptionId']
  newUser = {o: request.form[o] for o in requiredFields}
  newUser['accountCreated'] = datetime.now()
  print(newUser)
  Model.addNewUser(newUser)
  return Response(status=201)

@app.route('/')
def demo():
  return '<h1>Server running!</h1>'

if __name__ == '__main__':
  app.run(debug=True, threaded=True, port=5000)