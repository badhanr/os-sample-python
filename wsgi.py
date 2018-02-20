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
         VALUES ('mohan', 'Mac', 20, 'M', 7000)"""
    cursor.execute(sql)
    sql = "SELECT FIRST_NAME FROM EMPLOYEE \
       WHERE INCOME == '%d'" % (7000)
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          fname = row[0]
          # Now print fetched result
          return(fname)
    except:
       print "Error: unable to fecth data"
    #return("test")

if __name__ == "__main__":
    application.debug = True
    application.run()
