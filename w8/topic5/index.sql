-- USE website;
-- select * from member;
-- select * from message;


-- 5.2
-- normal
-- SELECT * FROM member WHERE username='test' and password='test';

-- index speed up
-- CREATE INDEX idx_username_password ON member (username, password);


-- 5.3
EXPLAIN SELECT * FROM member WHERE username='test' and password='test';
