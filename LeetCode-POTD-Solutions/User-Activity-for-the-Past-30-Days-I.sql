SELECT 
    TO_CHAR(activity_date, 'YYYY-MM-DD') AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE '2019-07-27' - 29
                        AND DATE '2019-07-27'
GROUP BY activity_date
ORDER BY activity_date;
