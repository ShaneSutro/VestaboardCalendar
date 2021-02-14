from database.firestore import db

scheduleRef = db.collection('schedules')

class Schedule():

  @staticmethod
  def getAll():
    return scheduleRef.get()