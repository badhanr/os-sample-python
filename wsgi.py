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
    DBh.add_case_subject("1234", "abc", "cde", "tesr", "test", "7/28/2018")
    
    
    return("test")
if __name__ == "__main__":
    application.debug = True
    application.run()
