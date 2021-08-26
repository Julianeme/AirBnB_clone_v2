-- script that creates the database hbnb_dev_db
-- also creates the MySQL new user hbnb_dev (in localhost)
-- sets the password of the new user to hbnb_dev_pwd
-- grants ALL privileges on the database hbnb_dev_db and
-- SELECT privileges on the performance_schema database

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db .* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema .* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
