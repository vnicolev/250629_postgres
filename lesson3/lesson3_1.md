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

---

## 新增資料的語法

```sql
INSERT INTO table1(column1, column2, …)
VALUES (value1, value2, …);
```

### 範例: 在 student 資料表新增一筆資料

```sql
INSERT INTO student (name, major)
VALUES ('呂育君', '歷史');
```

### 範例: 在 student 資料表新增多筆資料

```sql
INSERT INTO student (name, major)
VALUES ('王小柱', '生物'), ('陳信忠', '英文');
```

資料來源: https://neon.com/postgresql/postgresql-tutorial/postgresql-insert

---

## 更新資料的語法

```sql
UPDATE table_name
SET column1 = value1,
    column2 = value2,
    ...
WHERE condition;
```

### 範例: 在 student 資料表更新一筆資料

```sql
UPDATE student
SET name = '王阿柱',
    major = '物理'
WHERE student_id = 2;
```

資料來源: https://neon.com/postgresql/postgresql-tutorial/postgresql-update

---

## 刪除資料的語法

```sql
DELETE FROM table_name
WHERE condition;
```

### 範例: 在 student 資料表刪除一筆資料

```sql
DELETE FROM student
WHERE student_id = 2;
```

### 範例: 在 student 資料表刪除多筆資料

```sql
DELETE FROM student
WHERE major in ('歷史', '英文');
```

資料來源: https://neon.com/postgresql/postgresql-tutorial/postgresql-delete

---

## 選取資料的語法

```sql
SELECT
  select_list
FROM
  table1
WHERE
  columnA operator (
    SELECT
      columnB
    FROM
      table2
    WHERE
      condition
  )
ORDER BY
  columnB;
```

### 範例: 選取 student 的資料

```sql
SELECT
  *
FROM
  student
WHERE
  name='呂育君';
```
```sql
SELECT
  name, major
FROM
  student
WHERE
  name='呂育君';
```
```sql
SELECT
  *
FROM
  student
ORDER BY
  student_id ASC;
```
```sql
SELECT
  name, major
FROM
  student
ORDER BY
  student_id DESC
LIMIT
  3;
```

資料來源: https://neon.com/postgresql/postgresql-tutorial/postgresql-subquery

---

## 刪除資料表的語法

```sql
DROP TABLE [IF EXISTS] table_name
[CASCADE | RESTRICT];
```

### 範例: 刪除 student 的資料表

```sql
DROP TABLE IF EXISTS student;
```

資料來源: https://neon.com/postgresql/postgresql-tutorial/postgresql-drop-table