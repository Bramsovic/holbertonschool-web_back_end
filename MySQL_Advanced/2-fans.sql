-- Rank country origins of bands by their total number of fans.
-- Lists origins and their non-unique fan totals in descending order.
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
