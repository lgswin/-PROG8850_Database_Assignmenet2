-- Create the 'projects' table
CREATE TABLE IF NOT EXISTS projects2 (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);
-- Add the 'budget' column to the 'projects' table
ALTER TABLE projects2
ADD COLUMN budget DECIMAL(10,2);