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
    # Create table as per requirement
    sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

    cursor.execute(sql)
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    cursor.execute(sql)
    cursor.fetchall()
    return("done")
    
if __name__ == "__main__":
    application.run()
