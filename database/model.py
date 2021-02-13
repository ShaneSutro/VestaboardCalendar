from database.firestore import db
import database.users as users

class Users(object):
  def __init__(self, subscriberID='default', calendarType='default', calendarUrl='default', firstName='NoFirstName', lastName='NoLastName'):
    self.subscriberID = subscriberID
    self.calendarType = calendarType
    self.calendarUrl = calendarUrl
    self.firstName = firstName
    self.lastName = lastName

  @staticmethod
  def getAll():
    allUsers = users.userRef.get()
    return allUsers
