-- USE website;
-- CREATE TABLE users (
--     id BIGINT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique ID',
--     name VARCHAR(255) NOT NULL COMMENT 'Name',
--     username VARCHAR(255) NOT NULL COMMENT 'Username',
--     password VARCHAR(255) NOT NULL COMMENT 'Password',
--     follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',
--     time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time'
-- );

-- syntex Error
-- CREATE TABLE users (
--     id bigint PRIMARY KEY AUTO INCREMENT 'Unique ID',
--     name VARCHAR(255) NOT NULL 'Name',
--     username VARCHAR(255)NOT NULL 'Username',
--     password VARCHAR(255) NOT NULL 'Password',
--     follower_count int unsigned not null default to 0 'Follower Count',
--     time datetime not null default to current time 'Signup Time'
-- );



-- SHOW DATABASES website;

DESCRIBE member;
-- RENAME TABLE users TO member;

INSERT INTO users (name, username, password, follower_count, time)
VALUES ('John Doe', 'johndoe', 'password123', 0, NOW());
