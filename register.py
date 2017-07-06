# coding=utf-8
# -*- coding: utf-8 -*-
# author lzy

from selenium import webdriver
import time,datetime
import cx_Oracle



if __name__ == "__main__":
  conn = cx_Oracle.connect('username','password','tnsname')
  cursor=conn.cursor();
  sql='select f_sendurl,f_reportname from table where f_deflag = 0'
  cursor.execute(sql)
  rows =cursor.fetchall()
  for row in rows:
    capture(row[0],row[1])
  cursor.close()
  conn.close()
 def Oracle_Query(SqlStr, debug = 0):
    "Execute oracle query, and return datalist"
    datalist = []
    conn = cx_Oracle.connect(DB_UserName, DB_UserPwd, DB_ConnectStr)
    cursor = conn.cursor()
    try:
        cursor.execute(SqlStr)
        while 1:
            rs = cursor.fetchone()
            if rs == None:
                break
            datalist.append(rs)
        if debug:
            fieldnames = []
            for field in cursor.description:
                fieldnames.append(field[0])
            print fieldnames
            print datalist
            print "Query success!"
    except:
        print "Exec sql failed: %s" % SqlStr
    finally:
        cursor.close()
        conn.close()
        return datalist