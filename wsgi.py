#import pymysql
#import pymysql.cursors
#import mysql.connector
#conn= pymysql.connect(host='mysql://172.30.115.81:3306',user='userRTL',password='eNU1gYbC1EYLe6gN',db='sampledb',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
#a=conn.cursor()
#sql='CREATE TABLE `users` (`id` int(11) NOT NULL AUTO_INCREMENT,`email` varchar(255) NOT NULL,`password` varchar(255) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;'
#a.execute(sql)
import MySQLdb

# Open database connection
db = MySQLdb.connect("mysql://172.30.115.81:3306","userRTL","eNU1gYbC1EYLe6gN","sampledb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

