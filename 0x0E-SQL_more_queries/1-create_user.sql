-- script that creates the MySQL server user user_0d_1.
-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to the user user_0d_1
GRANT ALL ON *.* TO 'user_0d_1'@'localhost;
