WITH first_day AS (
    SELECT 
        player_id,
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
),
next_day AS (
    SELECT 
        f.player_id
    FROM first_day f
    JOIN Activity a
        ON f.player_id = a.player_id
       AND DATE_ADD(f.first_login, INTERVAL 1 DAY) = a.event_date
)
SELECT 
    ROUND(
        (SELECT COUNT(*) FROM next_day) / (SELECT COUNT(*) FROM first_day),
        2
    ) AS fraction;
