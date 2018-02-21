import MySQLdb

class DBHelper:
    
    def __init__(self, dbname="sampledb"):
        #self.dbname = dbname
        global db
        global conn
        db = MySQLdb.connect(host="172.30.115.81", port = 3306, user = "userRTL", passwd = "eNU1gYbC1EYLe6gN", db = "sampledb" )
        conn = db.cursor()

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS items (description char(50), owner char(50))"
        tblstmt2 = "CREATE TABLE IF NOT EXISTS cases (ticket_no char(50), log_date char(50), owner char(50), subject char(50), detail char(50),assignee char(50), department char(50), owner_fname char(50), owner_lname char(50), owner_phn char(10), owner_email char(50), owner_loc char(10), priority char(2), whd_ticket_id INT)"
        #itemidx = "CREATE INDEX IF NOT EXISTS itemIndex ON items (description ASC)" 
        #ownidx = "CREATE INDEX IF NOT EXISTS ownIndex ON items (owner ASC)"
        conn.execute(tblstmt)
        conn.execute(tblstmt2)
        #self.conn.execute(itemidx)
        #self.conn.execute(ownidx)
        db.commit()

    def add_item(self, item_text, owner): 
        stmt = "INSERT INTO items (description, owner) VALUES (%s, %s)"
        args = (item_text, owner)
        conn.execute(stmt, args)
        db.commit()

    def delete_item(self, item_text, owner):
        stmt = "DELETE FROM items WHERE description = (%s) AND owner = (%s)"
        args = (item_text, owner )
        conn.execute(stmt, args)
        db.commit()

    def get_items(self, owner):
        stmt = "SELECT description FROM items WHERE owner = (%s)"
        args = (owner,)
        conn.execute(stmt, args)
        results=conn.fetchall()
        for row in results:
           return row[0]
    
    def delete_chat(self,owner):
        #stmt = "UPDATE items SET description = '' WHERE owner = (?)"
        stmt = "DELETE FROM items WHERE owner = (%s)"
        args = (owner,)
        conn.execute(stmt, args)
        db.commit()

    def delete_case(self,ticket_no,owner):
        #stmt = "UPDATE items SET description = '' WHERE owner = (?)"
        stmt = "DELETE FROM cases WHERE ticket_no = (%s) and owner = (%s)"
        args = (ticket_no,owner)
        conn.execute(stmt, args)
        db.commit()

    def add_case_subject(self,ticket_no, text, chat, firstName, lastName, date_today):
        stmt = "INSERT into cases (ticket_no,log_date, owner, subject, owner_fname, owner_lname) values (%s,%s,%s,%s,%s,%s)"
        args = (ticket_no,date_today,chat,text,firstName,lastName)
        conn.execute(stmt, args)
        db.commit()

    def get_case_subject(self,ticket_no ,chat, date_today):
        stmt = "select * from cases where log_date = (%s) and owner = (%s) and ticket_no = (%s)"
        args = (date_today,chat,ticket_no)
        conn.execute(stmt, args)
        results=conn.fetchall()
        listRes=[]
        for row in results:
            listRes.append(row)
        #result = [x for x in conn.execute(stmt, args)]
        #print(result)
        #return results
        return listRes


    def get_case_department(self,ticket_no ,chat):
        stmt = "select department from cases where owner = (%s) and ticket_no = (%s)"
        args = (chat,ticket_no)
        conn.execute(stmt, args)
        result=conn.fetchone()
        #result = [x for x in conn.execute(stmt, args)]
        #print(result)
        return result

    def get_case_whd_ticket_id(self,ticket_no ,chat):
        stmt = "select whd_ticket_id from cases where owner = (%s) and ticket_no = (%s)"
        args = (chat,ticket_no)
        conn.execute(stmt, args)
        results= conn.fetchone()
        #for row in results:
            #return row[0]
        #result = [x for x in conn.execute(stmt, args)]
        #print(result)
        return results

    def delete_invalid_cases(self,chat):
        stmt = "delete from cases where (subject is NULL or (owner_phn is null and owner_loc is null)) and owner = (%s)"
        args = (chat,)
        conn.execute(stmt, args)
        db.commit()

    def update_case_detail(self,text, chat, date_today,ticket_no,department):
        stmt = "update cases set detail = (%s),department = (%s) where owner = (%s) and log_date = (%s) and ticket_no = (%s)"
        args = (text,department,chat,date_today,ticket_no)
        conn.execute(stmt, args)
        db.commit()

    def update_case_phn_loc(self,phn,loc, chat, date_today,assignee,ticket_no):
        stmt = "update cases set owner_phn = (%s), owner_loc = (%s), assignee = (%s) where owner = (%s) and log_date = (%s) and ticket_no = (%s)"
        args = (phn,loc,assignee,chat,date_today,ticket_no)
        conn.execute(stmt, args)
        db.commit()

    def update_whd_ticket_id(self,whd_ticket_id, owner, date_today,ticket_no):
        stmt = "update cases set whd_ticket_id = (%s) where owner = (%s) and log_date = (%s) and ticket_no = (%s)"
        args = (whd_ticket_id,owner, date_today, ticket_no)
        conn.execute(stmt, args)
        db.commit()

    def get_pending_case(self,chat):
        stmt = "select * from cases where owner = (%s)"
        args = (chat,)
        conn.execute(stmt, args)
        results=conn.fetchall()
        listRes=[]
        for row in results:
           listRes.append(row)
        return listRes
        #result = [x for x in conn.execute(stmt, args)]
        #print(result)
        #return result

    def update_priority(self,chat,priority,ticket_no):
        stmt = "update cases set priority = (%s) where owner = (%s) and ticket_no = (%s)"
        args = (priority,chat,ticket_no)
        conn.execute(stmt, args)
        db.commit()





