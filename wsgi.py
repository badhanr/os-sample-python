from flask import Flask
import MySQLdb
application = Flask(__name__)

@application.route("/")
def hello():
    # Open database connection
    db = MySQLdb.connect(host="172.30.115.81", port=3306, user="userRTL", passwd="eNU1gYbC1EYLe6gN", db="sampledb" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")
    
    #sql = """CREATE TABLE EMPLOYEE (
         #FIRST_NAME  CHAR(20) NOT NULL,
         #LAST_NAME  CHAR(20),
         #AGE INT,  
         #SEX CHAR(1),
         #INCOME FLOAT )"""
    #cursor.execute(sql)
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('drakshya', 'Mac', 20, 'F', 10000)"""
    cursor.execute(sql)
    cursor.commit()
    sql = "SELECT FIRST_NAME FROM EMPLOYEE WHERE INCOME =(?)"
    cursor.execute(sql,'10000',)
    results = cursor.fetchall()
    return(results)
    #return("test")

if __name__ == "__main__":
    application.debug = True
    application.run()
