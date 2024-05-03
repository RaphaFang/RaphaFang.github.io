-- 5.1.  Create a new table named message, in the website database. designed as below:
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

select * from member;
select * from message;


-- 5.2. JOIN 2 table
SELECT member.*, message.*
FROM member member
JOIN message message ON member.id = message.member_id;


-- 5.3. SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
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


-- 5.4. Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
-- -- SELECT FLOOR((SELECT SUM(like_count) FROM message)/ (SELECT COUNT(*) FROM member WHERE username = 'test')) AS average_like_count
-- SELECT 
--     member.username,
--     FLOOR((SELECT SUM(like_count) FROM joined_table WHERE username = 'test') / (SELECT COUNT(*) FROM member WHERE username = 'test')) AS average_like_count
-- FROM member member
-- JOIN message message ON member.id = message.member_id
-- WHERE member.username = 'test';

-- SELECT
--     member.username,
--     FLOOR(SUM(message.like_count) / COUNT(message.id)) AS average_like_count
-- FROM member member
-- JOIN message ON member.id = message.member_id
-- WHERE member.username = 'test';

-- >>> 10
SELECT
    username,
    FLOOR(SUM(like_count) / COUNT(message.id)) FROM member
JOIN message ON member.id = message.member_id
WHERE member.username = 'test';


-- 5.5. GROUP BY sender username
-- -- SELECT FLOOR((SELECT SUM(follower_count) FROM member) / (SELECT COUNT(*) FROM member)) AS average_like_count
-- SELECT
--     member.username,
--     FLOOR(SUM(message.like_count)/(COUNT(message.id))) AS average_like_count
-- FROM member member
-- JOIN message message ON member.id = message.member_id

-- GROUP BY member.username
-- ORDER BY member.username;
--  >>> 30

SELECT
    member.username,
    FLOOR(SUM(message.like_count)/(COUNT(message.id))) FROM member
JOIN message ON member.id = message.member_id
GROUP BY member.username
ORDER BY member.username;

-- SELECT * FROM member ORDER BY time DESC