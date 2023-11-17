#!/usr/bin/env python3
#
# Created on Sun Aug 13 2023
#
# Author: Deniz Küp
# Email: deniz.kp@gmail.com
# Description: Database adaptor for MySQL
#

import pymysql.cursors
from typing import Union

class DatabaseAdaptor:
    """ Class for MySQL database adaptor """
    def __init__(self,user_:str,password_:str,database_:str,host_:str = "localhost") -> None :
        self.USER     = user_;
        self.PASSWORD = password_;
        self.DATABASE = database_;
        self.HOST     = host_;
    
    def connectDb(self) -> pymysql.Connection :
        """ Initializes database connection wrt. credentials

        Returns:
            pymysql: pymysql object instance for database operations
        """
        return  pymysql.connect(user        = self.USER,
                                password    = self.PASSWORD,
                                database    = self.DATABASE,
                                host        = self.HOST,
                                cursorclass = pymysql.cursors.DictCursor)

    def fetchQuery(self,one:bool=False,query:str="") -> Union[None,dict,list]:
        """ Fetchs from database with given query string.

        Args:
            one (bool, optional): If true returns one result, otherwise all results. (Defaults to False.)
            query (str, optional): Database query. (Defaults to "".)

        Returns:
            fetch_result (None): None if query failed.
            fetch_result (dict): Result of the given query if one flag (fetch one) is True.
            fetch_result (list): Result of the given query if one flag (fetch all) is False.
        """
        result     = None
        connection = None
        try:
            connection = self.connectDb()
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone() if one else list(cursor.fetchall())

        except Exception as ex:
            print("[DATABASE ADAPTOR ERROR] Exception occured in `fetchQuery`! Exception : {}".format(ex))
            print("[DATABASE ADAPTOR ERROR] Query: {} ".format(query))
        
        finally:
            if(connection is not None):
                connection.close()
            return result
    
    def commitQuery(self,query:str) -> bool:
        """ Commits to database with given query string.

        Args:
            query (str): Database query.

        Returns:
            commit_result (bool): True if commit is successful, otherwise False.
        """
        result     = False
        connection = None
        try:
            connection = self.connectDb()
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
            result = True

        except Exception as ex:
            print("[DATABASE ADAPTOR ERROR] Exception occured in `commitQuery`! Exception : {}".format(ex))
            print("[DATABASE ADAPTOR ERROR] Query: {} ".format(query))
            
        finally:
            if(connection is not None):
                connection.close()
            return result
        