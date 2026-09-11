-- Create an index on the first letter of names.
-- Indexes only the first character of the name column.
CREATE INDEX idx_name_first
ON names (name(1));
