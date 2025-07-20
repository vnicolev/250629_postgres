### 1. 使用JOIN取出所有欄位

```sql
SELECT *
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊"
ON "車站代碼"="stationCode";
```
 
### 2. 做用JOIN取出指定欄位

```sql
SELECT "日期","進站人數","出站人數","stationName","name","stationAddrTw","haveBike"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼"="stationCode";
```

### 3. 取出基隆市有那些火車站

```sql
SELECT DISTINCT "stationName"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼"="stationCode"
WHERE "stationAddrTw" like '基隆市%';
```

### 4. 取出基隆火車站2022年3月1日資料

```sql
SELECT *
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼"="stationCode"
WHERE "日期" = '2022-03-01' AND "stationName" = '基隆'
```

### 5. 取出基隆火車站2022年3月份資料,時間由小到大排序

```sql
SELECT *
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼"="stationCode"
WHERE ("日期" BETWEEN '2022-03-01'AND '2022-03-31') AND "stationName" = '基隆'
ORDER BY "日期" ASC;
```

### 6. 取出基隆火車站和臺北火車站2022年3月份資料,時間由小到大排序

```sql
SELECT *
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼"="stationCode"
WHERE ("日期" BETWEEN '2022-03-01'AND '2022-03-31') AND "stationName" IN ('基隆','臺北')
ORDER BY "日期" ASC;
```

### 7. 取出資料進站人數最多的前10筆資料

```sql
SELECT *
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼"="stationCode"
ORDER BY "進站人數" DESC
LIMIT 10;
```

Source: https://github.com/roberthsu2003/python-SQLite-MySQL/tree/master/postgresSQL/%E7%B7%B4%E7%BF%92/8JOIN