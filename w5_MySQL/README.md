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

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/DESCRIBE_member.jpg)

===================================================================================================

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

見 3.2. 一次呈現

-- 3.2. 全選資料
SELECT all rows from the member table.

```ruby
SELECT * FROM member;
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/SELECT*FROM_member.png)

-- 3.3. 選擇全部 data，且降序排列
SELECT all rows from the member table, in descending order of time.

```ruby
SELECT * FROM member ORDER BY time DESC;
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/timeDESC.png)

-- 3.4. 降序排列，且選擇 2~4(排除 1), 這邊換行可以不用加上";"
SELECT total 3 rows, second to fourth, from the member table, in descending order of time.

```ruby
SELECT * FROM member ORDER BY time DESC
LIMIT 3 OFFSET 1;
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/3.4.png)

-- 3.5. 透過 username 篩選
SELECT rows where username equals to test.

```ruby
SELECT * FROM member
WHERE username = 'test';
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/3.5.png)

-- 3.6. 選擇 name 中包含 'es'

```ruby
SELECT * FROM member
WHERE name LIKE '%es%';
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/3.6.png)

-- 3.7. username and password equal to test

```ruby
SELECT * FROM member
WHERE username = "test" AND password = "test"
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/3.7.png)

-- 3.8. UPDATE data in name column to test2 where username equals to test.

```ruby
UPDATE member
SET name="test2"
WHERE name = "test";
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/3.8.png)

===================================================================================================

### task 4

===================================================================================================

### task 5
