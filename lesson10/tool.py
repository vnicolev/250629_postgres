import os
import psycopg2
import sys

from dotenv import load_dotenv

load_dotenv()

# 資料庫連線設定
DB_CONFIG = {
    "user": os.getenv('USER'),
    "password": os.getenv('PASSWORD'),
    "host": os.getenv('HOST'),
    "dbname": os.getenv('DBNAME'),
    "port": "5432"
}

def connect_to_database():
    """連接到 PostgreSQL 資料庫"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"資料庫連線錯誤: {e}")
        return None

def print_db_version(cursor):
    """列印資料庫版本"""
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"PostgreSQL 資料庫版本: {db_version[0]}")
    return db_version[0]

def print_station_count(cursor):
    """列印台鐵車站數量"""
    query = """
    SELECT count(*) as "筆數"
    FROM "台鐵車站資訊";
    """
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print(f"查詢結果: {result[0][0]} 筆資料")
    else:
        print("查無資料")

def print_station_name(cursor):
    """列印台鐵車站名稱"""
    query = """
    SELECT "stationName"
    FROM "台鐵車站資訊";
    """
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("台鐵車站名稱:")
        count = 1
        for row in result:
            print(f" {count} - {row[0]}")
            count += 1
    else:
        print("查無資料")

def get_station_name():
    try:
        conn = connect_to_database()
        if conn:
            print("成功連接到資料庫！")

            cursor = conn.cursor()
            # print_db_version(cursor)
            # print_station_count(cursor)
            # print_station_name(cursor)
            query = """
            SELECT "stationName"
            FROM "台鐵車站資訊";
            """
            cursor.execute(query)
            data = cursor.fetchall()
            if data:
                result = []
                for row in data:
                    result.append(row[0])
                else:
                    print("查無資料")            
            else:
                print("無法連接到資料庫，程式結束")
                sys.exit(1)

            # 關閉連接
            cursor.close()
            conn.close()
            print("資料庫連接已關閉")
            return result

    except psycopg2.Error as e:
        print(f"資料庫錯誤: {e}")    