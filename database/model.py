from database.firestore import db
import database.users as users
import database.schedules as schedules

class Model():
  def __init__(self):
    self.User = users.User()
    self.Schedule = schedules.Schedule()

  def getAllUsers(self):
    return self.User.getAll()

  def addNewUser(self, userData):
    return self.User.addUser(userData)

