-- 重新命名table
RENAME TABLE users TO member;

-- 顯示 Table Structure
DESCRIBE member;

-- 顯示 table data, Querying Data from the Table
SELECT * FROM member;

-- 3.1. 增加table data 資訊
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

-- 3.2. 全選資料
SELECT * FROM member;

-- 3.3. 選擇全部data，且降序排列
SELECT all rows from the member table, in descending order of time.
SELECT * FROM member ORDER BY time DESC;

-- 3.4. 降序排列，且選擇2~4(排除1), 這邊換行可以不用加上";"
SELECT * FROM member ORDER BY time DESC
LIMIT 3 OFFSET 1;
    -- 如果基於id 選擇用：WHERE id = 1;

-- 3.5. 透過username 篩選
SELECT * FROM member
WHERE username = 'test';

-- 3.6. 選擇name 中包含 'es'
SELECT * FROM member
WHERE name LIKE '%es%';

-- 3.7. username and password equal to test
SELECT * FROM member
WHERE username = "test" AND password = "test"

-- 3.8. UPDATE data in name column to test2 where username equals to test.
UPDATE member
SET name="test2"
WHERE name = "test";

SELECT * FROM member