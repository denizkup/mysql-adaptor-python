import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database_adaptor import DatabaseAdaptor

if __name__ == "__main__":
    dba = DatabaseAdaptor(user_="deniz",password_="deniz",database_="TEST",host_="localhost")
    fetch_result = dba.fetchQuery(one=False,query="SELECT * FROM USERS")
    print("Fetch Result : {}".format(fetch_result))

    commit_result = dba.commitQuery(query="UPDATE USERS SET NAME = 'new_user' WHERE ID = 50")
    print("Commit Result : {}".format(commit_result))

    

