-- SELECT * FROM member;


-- 4.1.  how many rows 
SELECT COUNT(*) FROM member; -- can add specific condition by using, WHERE AAA = 'BBB';
-- >>>> 5


-- 4.2. sum the value of followers 
SELECT SUM(follower_count) FROM member;   -- can add specific condition by using, WHERE AAA = 'BBB';
--  >>>> 100


-- 4.3.  the average of follower_count of all the rows
-- SELECT @count_member INT;  -- 有加上INT 意味著重新宣告，這就會報錯
-- SELECT COUNT(*) INTO @count_member FROM member;
-- SELECT @sum_follower INT;
-- SELECT SUM(follower_count) INTO @sum_follower FROM member;
-- SELECT @average_follower DECIMAL(10,2);  -- 可以加上DECIMAL(10,5) 10 只左邊的位數，5指小數點位數 
-- SELECT @average_follower:=FLOOR(@sum_follower/@count_member);

SET @count_member := (SELECT COUNT(*) FROM member);
SET @sum_follower := (SELECT SUM(follower_count) FROM member);
SET @average_follower := FLOOR(@sum_follower / @count_member);

SELECT @average_follower AS average_follower;

-- SELECT @count_member;  -- >>> 5
-- SELECT @sum_follower;  -- >>> 100
-- SELECT @average_follower;  -- >>>  20


-- 4.4.  the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
SELECT @count_member_2 := 2;
SELECT @sum_follower_2 := SUM(follower_count) FROM (
    SELECT follower_count
    FROM member
    ORDER BY follower_count DESC 
    LIMIT 2
) AS top_two_followers_alias;

SELECT @average_follower_2 := FLOOR(@sum_follower_2/@count_member_2);

-- SELECT @count_member_2 ;  -- >>> 2
-- SELECT @sum_follower_2 ;  -- >>> 70
-- SELECT @average_follower_2;  -- >>>  35