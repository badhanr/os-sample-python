import pymysql
import pymysql.cursors
import mysql.connector
conn= pymysql.connect(host='mysql://172.30.115.81:3306',user='userRTL',password='eNU1gYbC1EYLe6gN',db='sampledb',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
a=conn.cursor()
sql='CREATE TABLE `users` (`id` int(11) NOT NULL AUTO_INCREMENT,`email` varchar(255) NOT NULL,`password` varchar(255) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;'
a.execute(sql)
