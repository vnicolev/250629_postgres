#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
台鐵資料查詢系統 - 主程式
這是一個簡單的命令列介面程式，用於查詢台鐵車站資訊和進出站人數
"""
import tool
import streamlit as st

# establish localhost: `streamlit run main.py`

def main():
    """主程式"""
    st.title("台鐵車站名稱列表")
    result = tool.get_station_name()
    st.dataframe(result, width=400, height=600)

if __name__ == "__main__":
    main()