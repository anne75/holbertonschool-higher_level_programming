-- Create user user_0d_1
-- This user has all privileges
-- DROP USER IF EXISTS 'user_0d_1'@loclahost;
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
