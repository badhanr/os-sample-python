from flask import Flask
#import MySQLdb
from dbhelper import DBHelper
application = Flask(__name__)

@application.route("/")
def hello():
    DBh=DBHelper()
    DBh.setup()
    DBh.add_item("abc","def")
    DBh.delete_item("abc","def")
    DBh.get_items("def")
    DBh.delete_chat("def")
    DBh.delete_case("1234","def")
    DBh.add_case_subject("1234","abc", "cde", "tesr", "test", "7/28/2018")
    DBh.get_case_subject("1234" ,"abc","21/2/2018")
    DBh.get_case_department("1234","abc")
    DBh.get_case_whd_ticket_id("1234","abc")
    DBh.delete_invalid_cases("hjju")
    DBh.update_case_detail("yuc", "abc","21/2/2018","1234","1234")
    
    
    
    
    return("test")
if __name__ == "__main__":
    application.debug = True
    application.run()
