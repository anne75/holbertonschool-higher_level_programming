-- list all privileges for users user_0d_1 and user_0d_2
-- answer is the same wether user exists (with no privileges) or not
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
