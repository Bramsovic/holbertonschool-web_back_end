-- List Glam rock bands ranked by their lifespan up to 2024.
-- Computes each band's lifespan from its formed and split years.
SELECT band_name,
       IFNULL(split, 2024) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
