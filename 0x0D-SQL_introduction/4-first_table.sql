script that creates a table called first_table in the current database in your MySQL server.
CREATE TABLES first_table IF NOT Exist (
    id INT
    name VARCHAR(256)
);
