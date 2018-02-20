from flask import Flask
#import MySQLdb
from dbhelper import DBHelper
application = Flask(__name__)

@application.route("/")
def callingDB():
    # Open database connection
    #db = MySQLdb.connect(host="172.30.115.81", port=3306, user="userRTL", passwd="eNU1gYbC1EYLe6gN", db="sampledb" )
    # prepare a cursor object using cursor() method
    #cursor = db.cursor()
    # execute SQL query using execute() method.
    #cursor.execute("SELECT VERSION()")
    DBh=DBHelper()
    DBh.setup()
    return("test")
if __name__ == "__main__":
    application.debug = True
    application.run()
