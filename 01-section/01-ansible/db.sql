CREATE DATABSE employee_db;
CREATE USER 'db_user'@'localhost' IDENTIFIED BY 'Passw0rd';
GRANT ALL ON employee_db.* TO 'db_user'@'localhost';
USE employee_db;
CREATE TABLE employees (name VARCHAR(20));