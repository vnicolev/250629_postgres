## 建立資料表的語法

```sql
CREATE TABLE [IF NOT EXISTS] table_name (
   column1 datatype(length) column_constraint,
   column2 datatype(length) column_constraint,
   ...
   table_constraints
);
```

### 範例: 建立一個 student 的資料表

```sql
CREATE TABLE IF NOT EXISTS student (
   student_id SERIAL PRIMARY KEY,
   name VARCHAR(20) NOT NULL,
   major VARCHAR(20) UNIQUE
);
```

資料來源: https://neon.com/postgresql/postgresql-tutorial/postgresql-create-table