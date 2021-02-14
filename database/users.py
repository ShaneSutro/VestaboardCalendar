from database.firestore import db

userRef = db.collection('users')

class User(object):

  @staticmethod
  def getAll():
    return userRef.get()

  @staticmethod
  def addUser(user):
    r = userRef.document(user['subscriptionId']).set(user)
    print(r)