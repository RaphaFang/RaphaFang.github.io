USE website;
CREATE INDEX username_password_index ON member(username, password);
EXPLAIN SELECT * FROM member WHERE username='test' AND password='test';

select * from member;
DROP INDEX email_tel_index ON member;

select * from member;

-- 第5題
select * from message;

-- build new colimn, 'first_content_id',  'reply_content_id'
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
UPDATE message
SET reply_content_id=1
WHERE member_id = 3 AND content = 'the second piece of reply msg, to msg_1';