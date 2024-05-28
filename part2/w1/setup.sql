SHOW DATABASES;
USE basic_db;

CREATE TABLE processed_data (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    description TEXT,
    address TEXT,
    transport TEXT,
    mrt TEXT,
    lat REAL,
    lng REAL,
    images TEXT
);

select * from processed_data;
SELECT COUNT(*) FROM processed_data;

-- --------------------------------------------------------
-- the /api/mrts 
SELECT mrt, COUNT(*) as count
FROM processed_data
GROUP BY mrt
ORDER BY count DESC;