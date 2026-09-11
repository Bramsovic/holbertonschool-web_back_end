-- Create an index on the first letter of names and score.
-- Indexes only the first character of name and the score column.
CREATE INDEX idx_name_first_score
ON names (name(1), score);
