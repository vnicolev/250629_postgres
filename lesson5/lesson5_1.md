1. DBeaver 上選取要匯出的幾個表格
2. [右鍵] 產生SQL > DDL
3. 複製台鐵車站資訊與進出站人數的DDL
4. [右鍵] 匯出資料 > 匯出到CSV檔案
5. 保存DDL和CSV 
6. 下次要使用時先用DDL建表格再匯入CSV

```sql
-- public.台鐵車站資訊 definition

-- Drop table

-- DROP TABLE public.台鐵車站資訊;

CREATE TABLE public.台鐵車站資訊 (
	"stationCode" int4 NOT NULL,
	"stationName" varchar(50) NULL,
	"name" varchar(50) NULL,
	"stationAddrTw" varchar(50) NULL,
	"stationTel" varchar(50) NULL,
	gps varchar(50) NULL,
	"haveBike" varchar(50) NULL,
	CONSTRAINT 台鐵車站資訊_pkey PRIMARY KEY ("stationCode")
);


-- public.每日各站進出站人數 definition

-- Drop table

-- DROP TABLE public.每日各站進出站人數;

CREATE TABLE public.每日各站進出站人數 (
	日期 date NULL,
	車站代碼 int4 NULL,
	進站人數 int4 NULL,
	出站人數 int4 NULL,
	CONSTRAINT 每日各站進出站人數_車站代碼_fkey FOREIGN KEY (車站代碼) REFERENCES public.台鐵車站資訊("stationCode") ON DELETE SET NULL
);
```