### 1. 2022 各站點總進站人數

```sql
SELECT "name" AS "車站名", sum("進站人數") AS "進站人數", date_part('year', "日期") AS "年份", count("name") AS "筆數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "日期" BETWEEN '2022-01-01' AND '2022-12-31' 
GROUP BY "車站名" ,"年份"  -- 適用聚合函數
HAVING sum("進站人數") > 5000000  -- 適用聚合函數
ORDER BY "進站人數" DESC;
 ```

 ### 2. 基隆火車站 2020, 2021, 2022 每年進站人數 

```sql
SELECT "name" AS "車站名", sum("進站人數") AS "每年進站人數", date_part('year', "日期") AS "年份"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "name" = '基隆' or "name" = '臺北'
GROUP BY "車站名", "年份"  -- 適用聚合函數
HAVING date_part('year', "日期") BETWEEN 2020 AND 2022;  -- 適用聚合函數
 ```

 ### 3. 2022 平均每日進站人數超過 2 萬人的站點

```sql
SELECT "name" AS "車站名", avg("進站人數") AS "平均進站人數", date_part('year', "日期") AS "年份"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "stationCode" = "車站代碼"
GROUP BY "車站名", "年份"  -- 適用聚合函數
HAVING date_part('year', "日期") = 2022 AND avg("進站人數") > 20000;  -- 適用聚合函數
 ```