-- Create a trigger that resets valid_email when email changes.
-- Resets valid_email only if the user's email is updated.
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
SET NEW.valid_email = IF(NEW.email <> OLD.email, 0, NEW.valid_email);
