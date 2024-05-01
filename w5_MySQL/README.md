### task 2

```ruby
USE website;
CREATE TABLE member (
id BIGINT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID',
name VARCHAR(255) NOT NULL COMMENT 'Name',
username VARCHAR(255) NOT NULL COMMENT 'Username',
password VARCHAR(255) NOT NULL COMMENT 'Password',
follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time'
);
```

![Alt text](https://raphafang.github.io/w5_MySQL/img%20/mysql%3E%20DESCRIBE%20member.png "Optional Title")

### task 3

-- 3.1.增加 table data 資訊
INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.

```ruby
INSERT INTO member (name, username, password, follower_count)
VALUES ('test', 'test', 'test');
INSERT INTO member (name, username, password, follower_count)
VALUES ('arbitrary_1', 'ab1', '1234',"10");
INSERT INTO member (name, username, password, follower_count)
VALUES ('arbitrary_2', 'ab2', '1234',"20");
INSERT INTO member (name, username, password, follower_count)
VALUES ('arbitrary_3', 'ab3', '1234',"30");
INSERT INTO member (name, username, password, follower_count)
VALUES ('arbitrary_4', 'ab4', '1234',"40");
```

-- 3.2. 全選資料
SELECT all rows from the member table.

```ruby
SELECT \* FROM member;
```

![Alt text](/relative/path/to/img.jpg?raw=true "Optional Title")

-- 3.3. 選擇全部 data，且降序排列
SELECT all rows from the member table, in descending order of time.

```ruby
SELECT * FROM member ORDER BY time DESC;
```

mysql> SELECT \* FROM member ORDER BY time DESC;
|----+-------------+----------+----------+----------------+---------------------+
| id | name | username | password | follower_count | time |
+----+-------------+----------+----------+----------------+---------------------+
| 2 | arbitrary_1 | ab1 | 1234 | 10 | 2024-04-29 16:00:22 |
| 3 | arbitrary_2 | ab2 | 1234 | 20 | 2024-04-29 16:00:22 |
| 4 | arbitrary_3 | ab3 | 1234 | 30 | 2024-04-29 16:00:22 |
| 5 | arbitrary_4 | ab4 | 1234 | 40 | 2024-04-29 16:00:22 |
| 1 | test2 | test | test | 0 | 2024-04-29 15:54:39 |
+----+-------------+----------+----------+----------------+---------------------+
5 rows in set (0.00 sec)

### task 4

### task 5
