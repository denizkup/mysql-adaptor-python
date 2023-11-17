## MySQL adaptor for Python
An adaptor class to execute commit and fetch queries with MySQL and Python.

![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

#### Requirements
    pymysql

#### Usage
```python

from database_adaptor import DatabaseAdaptor

dba = DatabaseAdaptor(user_="username",password_="password",database_="database",host_="localhost")

fetch_result = dba.fetchQuery(one=False,query="SELECT * FROM USERS")
print("Fetch Result : {}".format(fetch_result))
# [{'ID': 50, 'NAME': 'user1'}, {'ID': 51, 'NAME': 'user2'}]

commit_result = dba.commitQuery(query="UPDATE USERS SET NAME = 'new_user' WHERE ID = 50")
print("Commit Result : {}".format(commit_result))
# True
```



    
