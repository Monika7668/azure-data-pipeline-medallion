-- Region-wise Revenue
SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region;

-- Top Performing Region
SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;

-- Revenue Distribution
SELECT region, COUNT(*) AS total_orders
FROM sales
GROUP BY region;
