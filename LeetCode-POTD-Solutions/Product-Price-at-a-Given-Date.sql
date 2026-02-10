SELECT 
    p.product_id,
    COALESCE(pr.new_price, 10) AS price
FROM 
    (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN (
    SELECT p1.product_id, p1.new_price
    FROM Products p1
    JOIN (
        SELECT product_id, MAX(change_date) AS last_date
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    ) p2
    ON p1.product_id = p2.product_id
    AND p1.change_date = p2.last_date
) pr
ON p.product_id = pr.product_id
ORDER BY p.product_id;
