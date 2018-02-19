from flask import Flask
import MySQLdb
application = Flask(__name__)

@application.route("/")
def hello():
    # Open database connection
    db = MySQLdb.connect("mysql://172.30.115.81:3306","userRTL","eNU1gYbC1EYLe6gN","sampledb" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")
    return "0"
    
if __name__ == "__main__":
    application.run()
