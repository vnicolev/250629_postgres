#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
台鐵資料查詢系統 - 主程式
這是一個簡單的命令列介面程式，用於查詢台鐵車站資訊和進出站人數
"""

import psycopg2
import sys

# 資料庫連線設定
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "password",
    "host": "host.docker.internal",
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

def main():
    """主程式"""
    conn = connect_to_database()
    if conn:
        print("成功連接到資料庫！")

        # 測試連接是否成功
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"PostgreSQL 資料庫版本: {db_version[0]}")

        # 查詢資料庫
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

    else:
        print("無法連接到資料庫，程式結束")
        sys.exit(1)

    # 關閉連接
    cursor.close()
    conn.close()
    print("資料庫連接已關閉")

if __name__ == "__main__":
    main()