# SQLITE
安装: `sudo apt-get install sqlite3`

创建数据库:`sqlite3 dbname.db` 

### 数据表  

* 创建表:
``` 
CREATE TABLE DBNAME.TABLENAME (
    COLUMN1 DATATYPE,
    COLUMN2 DATATYPE,
    PRIMARY KEY (COLUMN1,COLUMN2)
);
```
>查看所有的表:   .TABLES  
>查看表的完整信心:   .SCHEMA TABLENAME  
>删除表:DROP TABLE TABLENAME;

### 数据操作
* 插入数据:  
```
1.INSERT INTO TABLENAME [(COLUMN1,COLUMN2,COLUMN3)] VALUES (VALUE1,VALUE2,VALUE3);
2.INSERT INTO TABLENAME VALUES (VALUE1,VALUE2,VALUE3);
3.INSERT INTO TABLENAME [(COLUMN1,COLUMN2,COLUMN3)] SELECT COLUMN1,COLUMN2,COLUMN3 FROM TABLENAME ;
```
* 查询数据:  
```
1.SELECT * FROM TABLENAME;
2.SELECT COLUMN1,COLUMN2,COLUMN3 FROM TABLENAME;
```
* 更新数据:
```
UPDATE TABLENAME SET COLUMN1 = VALUE1,COLUMN2 = VALUE2 WHERE ID = '1';
```
* 删除数据:
```
DELETE FROM TABLENAME WHERE ID = '1';
```
* 限制数据输出数量:
```
1.SELECT * FROM TABLENAME LIMIT 6;
2.SELECT * FROM TABLENAME LIMIT 3 OFFSET 2;
//LIMIT 输出行数 OFFSET 从下一行开始输出
```
* 数据排序:
```
1.SELECT * FROM TABLENAME ORDER BY COLUMN1,COLUMN2 ASC;//升序
2.SELECT * FROM TABLENAME ORDER BY COLUMN1,COLUMN2 DESC;//降序
```
* 数据分组:
```
1.SELECT COLUMN1 SUM(COLUMN2) FROM TABLENAME GROUP BY COLUMN1;
2.SELECT COLUMN1 SUM(COLUMN2) FROM TABLENAME GROUP BY COLUMN1 ORDER BY COLUMN DESC;//分组排序
```
* 分组过滤:
```
SELECT COLUMN1,COUNT(COLUMN2) FROM TABLENAME GROUP BY COLUMN1 HAVING COUNT(COLUMN2)>1;
```
* 排除重复记录:
``` 
SELECT DESTINCT * FROM TABLENAME;
```
### 约束
`NOT NULL`:不能为空  
`DEFAULT`:当某列没有指定值时，为该列提供默认值  
```
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL    DEFAULT 50000.00
);
```
`UNIQUE`:确保某列中的所有值是不同的  
```
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL UNIQUE,
   ADDRESS        CHAR(50),
   SALARY         REAL    DEFAULT 50000.00
);
```
`PRIMARY Key`:唯一标识数据库表中的各行/记录  
```
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```
`CHECK`:CHECK 约束确保某列中的所有值满足一定条件  
```
CREATE TABLE COMPANY3(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL    CHECK(SALARY > 0)
);
```
### 连表
* 交叉连接:
```
SELECT EMP_ID, NAME, DEPT FROM COMPANY CROSS JOIN DEPARTMENT;(表的条数为COMPANY*COMPANY)
```
* 内连表:
```
SELECT EMP_ID, NAME, DEPT FROM COMPANY INNER JOIN DEPARTMENT ON COMPANY.ID = DEPARTMENT.EMP_ID;
```
* 外连表:
```
SELECT EMP_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT ON COMPANY.ID = DEPARTMENT.EMP_ID;
```
### 集合
`UNION`:合并两个或多个 SELECT 语句的结果，不返回任何重复的行  
```
SELECT EMP_ID, NAME, DEPT FROM COMPANY INNER JOIN DEPARTMENT ON COMPANY.ID = DEPARTMENT.EMP_ID
UNION
SELECT EMP_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT ON COMPANY.ID = DEPARTMENT.EMP_ID;
```
`UNION ALL`:结合两个 SELECT 语句的结果，包括重复行  
```
SELECT EMP_ID, NAME, DEPT FROM COMPANY INNER JOIN DEPARTMENT ON COMPANY.ID = DEPARTMENT.EMP_ID
UNION ALL
SELECT EMP_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT ON COMPANY.ID = DEPARTMENT.EMP_ID;
```
### 触发器:
```
CREATE  TRIGGER trigger_name [BEFORE|AFTER] UPDATE OF column_name 
ON table_name
BEGIN
 -- Trigger logic goes here....
END;
```
>(table_name 上的 INSERT、DELETE 和 UPDATE)
```
CREATE TRIGGER audit_log AFTER INSERT ON COMPANY
BEGIN
   INSERT INTO AUDIT(EMP_ID, ENTRY_DATE) VALUES (new.ID, datetime('now'));
END;
```
* 列出触发器:
```
SELECT name FROM sqlite_master WHERE type = 'trigger';
```
* 删除触发器:
```
DROP TRIGGER trigger_name
```
### 索引:
* 单列索引:只基于表的一个列上创建的索引  
```
CREATE INDEX index_name ON table_name (column_name);
```
* 唯一索引:唯一索引不仅是为了性能，同时也为了数据的完整性。唯一索引不允许任何重复的值插入到表中  
```
CREATE UNIQUE INDEX index_name ON table_name (column_name);
```
* 组合索引:组合索引是基于一个表的两个或多个列上创建的索引  
```
CREATE INDEX index_name ON table_name (column1, column2);
```
>注: 
>是否要创建一个单列索引还是组合索引，要考虑到您在作为查询过滤条件的 WHERE 子>句中使用非常频繁的列。
>如果值使用到一个列，则选择使用单列索引。如果在作为过滤的 WHERE 子句中有两个>或多个列经常使用，则选择使用组合索引
>隐式索引:在创建对象时，由数据库服务器自动创建的索引。索引自动创建为主键约束>和唯一约束
* 删除索引:
```
DROP INDEX salary_index;
```
* 指定索引查询:
```
SELECT * FROM COMPANY INDEXED BY salary_index WHERE salary > 5000;
```
### ALTER关键字:
* 表重命名:
```
ALTER TABLE COMPANY RENAME TO OLD_COMPANY;
```
* 表添加字段:
```
ALTER TABLE OLD_COMPANY ADD COLUMN SEX char(1);
```
### 视图:
* 创建视图:
```
CREATE VIEW COMPANY_VIEW AS
SELECT ID, NAME, AGE FROM  COMPANY;
```
* 删除视图:
```
DROP VIEW view_name;
```
### 事务:
> 以逻辑顺序完成的工作单位或序列，可以是由用户手动操作完成，也可以是由某种数据库程序自动完成  
>`BEGIN TRANSACTION`：开始事务处理  
>`COMMIT`：保存更改，或者可以使用 END TRANSACTION 命令  
>`ROLLBACK`：回滚所做的更改

* 开始一个事务，并从表中删除 age = 25 的记录，最后，我们使用 ROLLBACK 命令撤消所有的更改  
```
BEGIN;
DELETE FROM COMPANY WHERE AGE = 25;
ROLLBACK;
```
* 开始另一个事务，从表中删除 age = 25 的记录，最后我们使用 COMMIT 命令提交所有的更改
```
BEGIN;
DELETE FROM COMPANY WHERE AGE = 25;
COMMIT;
```
### 自动递增:
```
CREATE TABLE COMPANY(
   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
   NAME           TEXT      NOT NULL,
   AGE            INT       NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```
### 日期&时间
> `date(timestring, modifier, modifier, ...)`:以 YYYY-MM-DD 格式返回日期  
> `time(timestring, modifier, modifier, ...)`:以 HH:MM:SS 格式返回时间  
> `datetime(timestring, modifier, modifier, ...)`:以 YYYY-MM-DD HH:MM:SS 格式返回  
> `julianday(timestring, modifier, modifier, ...)`:这将返回从格林尼治时间的公元前 4714 年 11 月 24 日正午算起的天数。  
> `strftime(format, timestring, modifier, modifier, ...)`:这将根据第一个参数指定的格式字符串返回格式化的日期。具体格式见下边讲解  

* 时间字符串:
>YYYY-MM-DD  
>YYYY-MM-DD HH:MM  
>YYYY-MM-DD HH:MM:SS.SSS  
>MM-DD-YYYY HH:MM  
>HH:MM  
>YYYY-MM-DDTHH:MM  
>HH:MM:SS  
>YYYYMMDD HHMMSS  
>now

* 时间修饰符:
>NNN {days|hours|minutes|months|years}  
>NNN.NNNN seconds  
>start of {month|year|day}  
>weekday N  
>unixepoch
>localtime
>utc

下面是计算当前月份的最后一天  
```
SELECT date('now','start of month','+1 month','-1 day'); 
``` 
计算当年 10 月的第一个星期二的日期  
```
SELECT date('now','start of year','+9 months','weekday 2');
```
计算给定 UNIX 时间戳 1092941466 的日期和时间
```
SELECT datetime(1092941466, 'unixepoch');
```
计算给定 UNIX 时间戳 1092941466 相对本地时区的日期和时间
```
SELECT datetime(1092941466, 'unixepoch', 'localtime');
```
以utc格式化日期
```
SELECT time('12:00', 'utc');
```

* strftime()格式化任何日期和时间
>%d:一月中的第几天，01-31  
>%f:带小数部分的秒，SS.SSS  
>%H:小时，00-23  
>%j:一年中的第几天，001-366  
>%J:儒略日数，DDDD.DDDD  
>%m:月，00-12  
>%M:分，00-59  
>%s:从 1970-01-01 算起的秒数  
>%S:秒，00-59  
>%w:一周中的第几天，0-6 (0 is Sunday)  
>%W:一年中的第几周，01-53  
>%Y:年，YYYY

计算当前的 UNIX 时间戳  
```
SELECT strftime('%s','now');
```