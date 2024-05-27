USE website;
CREATE INDEX username_password_index ON member(username, password);
EXPLAIN SELECT * FROM member WHERE username='test' AND password='test';



-- 第5題
select * from message;

-- build new column, 'first_content_id',  'reply_content_id'
ALTER TABLE message
ADD COLUMN first_content_id INT NULL;
ALTER TABLE message
ADD COLUMN reply_content_id INT NULL;

-- insert new reply content
INSERT INTO message (member_id, content, first_content_id, reply_content_id)
VALUES (1, '並非回復的一則留言', 2, NULL);
INSERT INTO message (member_id, content, first_content_id, reply_content_id)
VALUES (2, 'a piece of reply msg, to msg_1', NULL, 1);
INSERT INTO message (member_id, content, first_content_id, reply_content_id)
VALUES (3, 'the second piece of reply msg, to msg_1', NULL, 1);

-- select the specific content & its replies
SELECT * FROM message WHERE first_content_id = 1 OR reply_content_id = 1;

-- the omission that have to deal
-- 1. reply's reply
-- 2. (done)different content from the same user(might occur while adopting member_id as the key)



-- 第6題
ALTER TABLE message
ADD COLUMN tag VARCHAR(255) NULL;

-- UPDATE new tag content
UPDATE message
SET tag="python"
WHERE  member_id=3 AND reply_content_id = 1;

UPDATE message
SET tag="js"
WHERE  member_id=1 AND first_content_id = 1;

-- select the specific tag
SELECT * FROM message WHERE tag = 'python';

-- 這樣的設計無法解決一個問題，如果存在多個以上的tag?