from flask import Flask
#import MySQLdb
from dbhelper import DBHelper
application = Flask(__name__)

@application.route("/")
def hello():
    DBh=DBHelper()
    DBh.setup()
    DBh.add_item("abc","def")
    DBh.add_item("123","456")
    
    #DBh.delete_item("abc","def")
    res1=DBh.get_items("def")
    res2=DBh.get_items("456")
    #print(res1)
    #DBh.delete_chat("def")
    #DBh.delete_case("1234","def")
    #DBh.add_case_subject("ticket number 1","text", "chat", "firstname", "lastname", r"21/2/2018")
    #DBh.add_case_subject("ticket number 2","text2", "chat2", "firstname2", "lastname2", r"21/2/2017")
    #DBh.add_case_subject("ticket number 2","text2", "chat", "firstname2", "lastname2", r"21/2/2017")
    #res3=DBh.get_case_subject("ticket number 2" ,"chat2", r"21/2/2017")
    #print(res2)
    #DBh.update_case_detail("detail2", "chat2",r"21/2/2017","ticket number 2","department 2")
    #DBh.update_case_phn_loc("7894455612","Pune", "chat2",r"21/2/2017","Elon","ticket number 2")
    #res4=DBh.get_case_subject("ticket number 2" ,"chat2",r"21/2/2017")
    
    #res5=DBh.get_case_department("ticket number 2","chat2")
    #print(res3)
    #res6=DBh.get_case_whd_ticket_id("ticket number 2","chat2")
    #print(res4)
    #DBh.delete_invalid_cases("hjju")
    
   
    #DBh.update_whd_ticket_id("whd_ticket_id", "chat2",r"21/2/2017","ticket number 2")    
    #res7=DBh.get_pending_case("chat2")
    #print(res5)
    #DBh.update_priority("abc","2","1234569")
    #return(str(res1)+"\n"+str(res2)+"\n"+str(res3)+"\n"+str(res4)+"\n"+str(res5)+"\n"+str(res6)+"prnding cases"+str(res7))
    return(str(res1)+"\n"+str(res2))
    #return("test")
    
if __name__ == "__main__":
    application.debug = True
    application.run()
