import sqlite3

def get_user(uid):
    conn = sqlite3.connect('D:\workspace\건강검진데이터분석\db_sqlite\project.db')
    cur = conn.cursor()

    sql = 'select * from user where uid=?'
    cur.execute(sql, (uid,))
    row = cur.fetchone()

    cur.close()
    conn.close()
    return row

def get_disease(uid):
    conn = sqlite3.connect('D:\workspace\건강검진데이터분석\db_sqlite\project.db')
    cur = conn.cursor()

    sql = 'select * from disease where uid=?'
    cur.execute(sql, (uid,))
    row = cur.fetchall()

    cur.close()
    conn.close()
    return row

def insert_user(params):
    conn = sqlite3.connect('D:\workspace\건강검진데이터분석\db_sqlite\project.db')
    cur = conn.cursor()

    sql = 'insert into user values (?, ?, ?, ?, ?, ?)'
    cur.execute(sql, params)
    conn.commit()

    cur.close()
    conn.close()

def insert_disease(params):
    conn = sqlite3.connect('D:\workspace\건강검진데이터분석\db_sqlite\project.db')
    cur = conn.cursor()

    sql = 'insert into disease values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cur.execute(sql, params)
    conn.commit()

    cur.close()
    conn.close()

def get_user_list():
    conn = sqlite3.connect('D:\workspace\건강검진데이터분석\db_sqlite\project.db')
    cur = conn.cursor()

    sql = 'select * from user'
    cur.execute(sql)
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows

def update_user(params):
    conn = sqlite3.connect('D:\workspace\건강검진데이터분석\db_sqlite\project.db')
    cur = conn.cursor()

    sql = 'update user set pwd=?, uname=?, email=? where uid=?'
    cur.execute(sql, params)
    conn.commit()

    cur.close()
    conn.close()

def delete_user(uid):
    conn = sqlite3.connect('D:\workspace\건강검진데이터분석\db_sqlite\project.db')
    cur = conn.cursor()

    sql = 'delete from user where uid=?'
    cur.execute(sql, (uid,))
    conn.commit()

    cur.close()
    conn.close()