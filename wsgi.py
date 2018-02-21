from flask import Flask
#import MySQLdb
from dbhelper import DBHelper
application = Flask(__name__)

@application.route("/")
def hello():
    DBh=DBHelper()
    DBh.setup()
    DBh.add_item("abc","def")
    
    #DBh.delete_item("abc","def")
    res1=DBh.get_items("def")
    print(res1)
    #DBh.delete_chat("def")
    #DBh.delete_case("1234","def")
    DBh.add_case_subject("1234","abc", "cde", "tesr", "test", "7/28/2018")
    DBh.update_case_detail("yuc", "abc","21/2/2018","1234","1234")
     DBh.update_case_phn_loc("7894455612","Pune", "abc","21/2/2018","Elon","1234")
    res2=DBh.get_case_subject("1234" ,"abc","21/2/2018")
    print(res2)
    res3=DBh.get_case_department("1234","abc")
    print(res3)
    res4=DBh.get_case_whd_ticket_id("1234","abc")
    print(res4)
    #DBh.delete_invalid_cases("hjju")
    
   
    DBh.update_whd_ticket_id("1234569", "Elon","21/2/2018","1234")    
    res5=DBh.get_pending_case("abch")
    print(res5)
    DBh.update_priority("abc","2","1234569")
    return(str(res1)+str(res2)+str(res3)+str(res4)+str(res5))
    #return("test")
if __name__ == "__main__":
    application.debug = True
    application.run()
