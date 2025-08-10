#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
台鐵資料查詢系統 - 主程式
這是一個簡單的命令列介面程式，用於查詢台鐵車站資訊和進出站人數
"""
import tool

def main():
    """主程式"""
    result = tool.get_station_name()
    for station in result:
        print(station)

if __name__ == "__main__":
    main()