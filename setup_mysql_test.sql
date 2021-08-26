-- script that creates the database hbnb_test_db
-- also creates the MySQL new user hbnb_test (in localhost)
-- sets the password of the new user to hbnb_test_pwd
-- grants ALL privileges on the database hbnb_test_db and
-- SELECT privileges on the performance_schema database

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db .* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema .* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
