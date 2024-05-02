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
WHERE username = "test";
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/3.8.png)

===================================================================================================

### task 4

-- 4.1. how many rows

```ruby
SELECT COUNT(*) FROM member;
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/4.1.png)

-- 4.2. sum the value of followers

```ruby
SELECT SUM(follower_count) FROM member;
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/4.2.png)

-- 4.3. the average of follower_count of all the rows

```ruby
SET @count_member := (SELECT COUNT(*) FROM member);
SET @sum_follower := (SELECT SUM(follower_count) FROM member);
SET @average_follower := FLOOR(@sum_follower / @count_member);

SELECT @average_follower AS average_follower;
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/4.3.png)

-- 4.4. the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.

```ruby
SELECT @count_member_2 := 2;
SELECT @sum_follower_2 := SUM(follower_count) FROM (
SELECT follower_count
FROM member
ORDER BY follower_count DESC
LIMIT 2
) AS top_two_followers_alias;

SELECT @average_follower_2 := FLOOR(@sum_follower_2/@count_member_2);
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/4.4.png)

===================================================================================================

### task 5

-- 5.1. Create a new table named message, in the website database. designed as below:

```ruby
USE website;
CREATE table message (
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
    member_id BIGINT not null COMMENT 'Member ID for Message Sender',
    content VARCHAR(255) NOT NULL COMMENT 'Content',
    like_count int unsigned not null DEFAULT 0 COMMENT 'Like Count',
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',
    FOREIGN KEY (member_id) REFERENCES member(id)
    );

INSERT INTO message (member_id, content, like_count)
VALUES ('1', 'txt from member_id 1', '10');
INSERT INTO message (member_id, content, like_count)
VALUES ('2', 'hi from member_id 2', "20");
INSERT INTO message (member_id, content, like_count)
VALUES ('3', 'hello from member_id 3', "30");
INSERT INTO message (member_id, content, like_count)
VALUES ('4', 'good night from member_id 4', "40");
INSERT INTO message (member_id, content, like_count)
VALUES ('5', 'end from member_id 5', "50");
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/5.1.png)

-- 5.2. JOIN 2 table

```ruby
SELECT member.*, message.*
FROM member member
JOIN message message ON member.id = message.member_id;
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/5.2.png)

-- 5.3. SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.

```ruby
CREATE temporary TABLE joined_table AS
SELECT
    member.id,
    member.name,
    member.username,
    member.password,
    member.follower_count,
    member.time AS member_time,

    message.id AS message_id,
    message.member_id,
    message.content,
    message.like_count,
    message.time AS message_time
FROM member member
LEFT JOIN message message ON member.id = message.member_id;

SELECT * from joined_table
WHERE username = 'test';
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/5.3.png)

-- 5.4. Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.

```ruby
SELECT
    member.username,
    FLOOR(SUM(message.like_count) / COUNT(message.id)) AS average_like_count
FROM member member
JOIN message ON member.id = message.member_id
WHERE member.username = 'test';
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/5.4.png)

-- 5.5. GROUP BY sender username

```ruby
SELECT
    member.username,
    FLOOR(SUM(message.like_count)/(COUNT(message.id))) AS average_like_count
FROM member member
JOIN message message ON member.id = message.member_id

GROUP BY member.username
ORDER BY member.username;
```

![Optional Title](https://raw.githubusercontent.com/RaphaFang/RaphaFang.github.io/main/w5_MySQL/img/5.5.png)
