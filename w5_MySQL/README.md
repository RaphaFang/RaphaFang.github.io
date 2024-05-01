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

mysql> DESCRIBE member;
+----------------+--------------+------+-----+-------------------+-------------------+
| Field | Type | Null | Key | Default | Extra |
+----------------+--------------+------+-----+-------------------+-------------------+
| id | bigint | NO | PRI | NULL | auto_increment |
| name | varchar(255) | NO | | NULL | |
| username | varchar(255) | NO | | NULL | |
| password | varchar(255) | NO | | NULL | |
| follower_count | int unsigned | NO | | 0 | |
| time | datetime | NO | | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+----------------+--------------+------+-----+-------------------+-------------------+
6 rows in set (0.01 sec)

### task 3

### task 4

### task 5
