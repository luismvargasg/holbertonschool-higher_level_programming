-- Script that creates the table unique_id on your MySQL server
-- where id must be a unique value set to 1 by dafault.
CREATE IF NOT EXISTS unique_id (
    id INT PRIMARY KEY DEFAULT 1,
    name VARCHAR(256)
);
