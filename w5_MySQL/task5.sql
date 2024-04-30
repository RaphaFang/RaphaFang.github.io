-- 5.1.  Create a new table named message, in the website database. designed as below:
-- USE website;
-- CREATE table message (
--     id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
--     member_id BIGINT not null COMMENT 'Member ID for Message Sender',
--     content VARCHAR(255) NOT NULL COMMENT 'Content',
--     like_count int unsigned not null DEFAULT 0 COMMENT 'Like Count', 
--     time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',
--     FOREIGN KEY (member_id) REFERENCES member(id)
--     );

select * from message;