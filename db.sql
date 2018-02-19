create table emp
(
    name varchar(64) primary key,
    
);
INSERT INTO emp(name)VALUES ('Mac')
sql = "SELECT * FROM EMPLOYEE
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      # Now print fetched result
      print "fname=%s"(fname)
except:
   print "Error: unable to fecth data"
