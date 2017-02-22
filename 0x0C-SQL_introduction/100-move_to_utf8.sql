-- Convert a database, a table and one of its column to utf8mb4
-- https://mathiasbynens.be/notes/mysql-utf8mb4
USE hbtn_0c_0;

ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

ALTER TABLE first_table
CONVERT TO CHARACTER
SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
CHANGE `name` `name` VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
