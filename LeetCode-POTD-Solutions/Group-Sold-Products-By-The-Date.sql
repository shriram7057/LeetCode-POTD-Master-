WITH t AS (
    SELECT DISTINCT 
        sell_date,
        product
    FROM Activities
)
SELECT
    TO_CHAR(sell_date, 'YYYY-MM-DD') AS sell_date,
    COUNT(product) AS num_sold,
    LISTAGG(product, ',') WITHIN GROUP (ORDER BY product) AS products
FROM t
GROUP BY sell_date
ORDER BY sell_date;
