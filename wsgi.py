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
         VALUES ('Madan', 'Mac', 20, 'M', 5000)"""
    cursor.execute(sql)
    sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          fname = row[0]
          lname = row[1]
          age = row[2]
          sex = row[3]
          income = row[4]
          # Now print fetched result
          return(print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                 (fname, lname, age, sex, income ))
    except:
       print "Error: unable to fecth data"
    #return("test")

if __name__ == "__main__":
    application.debug = True
    application.run()
