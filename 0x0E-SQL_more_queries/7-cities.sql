-- script that creates the database hbtn_0d_usa and the tabe cities.
-- creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    `id` INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
