-- USE website;
-- select * from member;
-- select * from message;


-- 5.2
-- normal
SELECT * FROM member WHERE username='test' and password='test';

-- index speed up
CREATE INDEX idx_username_password ON member (username, password);


-- 5.3
EXPLAIN SELECT * FROM member WHERE username='test' and password='test';

-- 5.4

-- 5.5
CREATE INDEX like_testing_index ON member (username);
-- 'LIKE abc' is equivalent to '= abc'

-- prefix matches
EXPLAIN SELECT * FROM member WHERE username LIKE 'ab%';
-- suffix matches
EXPLAIN SELECT * FROM member WHERE username LIKE '%4';