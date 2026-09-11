-- Create a function that safely divides two integers.
DELIMITER $$
-- Returns zero when the divisor is zero, otherwise returns the quotient.
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
NO SQL
BEGIN
    IF b = 0 THEN
        RETURN 0;
    END IF;
    RETURN a / b;
END$$
DELIMITER ;
