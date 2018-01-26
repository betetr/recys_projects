# -*- coding:utf8 -*-
import pymysql
import pandas as pd


def connectMysql():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1994',
                                db='recys', charset='utf8')
    # cursor = conn.cursor()
    return conn

def distinct_user():
    conn = connectMysql()
    cursor = conn.cursor()
    sql = "select distinct user_id from train_user limit 10;"
    cursor.execute(sql)
    dist_user = []
    for each in cursor.fetchall():
        print(each)
        dist_user.append(each[0])
    cursor.close()
    # with open("..//dataset//distinct_user_id.txt", 'w') as fw:
    #     fw.write("%s" % '\n'.join(dist_user))


if __name__ == "__main__":
    f = open("..//dataset//distinct_user_id.txt", 'r')
    dis_user = []
    for l in f.readlines():
        # print(l.replace("\n", ""))
        dis_user.append(l.replace("\n", ""))
    dis_user = tuple(dis_user)
    print(dis_user[0:10])
    print(dis_user[0], dis_user[9])
    conn = connectMysql()
    # cursor = conn.cursor()
    sql = 'select * from train_user where user_id in (%s)' % ','.join(dis_user[9000:10000])
    # cursor.execute(sql)
    # i=0
    # for each in cursor.fetchall():
    #     i+=1
    #     print(i,each)
    # cursor.close()

    df = pd.read_sql(sql, conn)
    df.to_csv("..//dataset//9000_9999_user_info.csv")
    print(df[0:10])