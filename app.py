from flask import Flask, request, jsonify, Response
import database.firestore as firestore
import database.model as model
app = Flask(__name__)

@app.route('/')
def demo():
  return '<h1>Server running!</h1>'

@app.route('/users')
def handleUsers():
  users = model.Users().getAll()
  for user in users:
    print(user.id)
    print(user.to_dict())
  return Response(200)


if __name__ == '__main__':
  app.run(debug=True, threaded=True, port=5000)