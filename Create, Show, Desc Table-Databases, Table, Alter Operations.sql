# 1. Basic SQL Commands

# Create a database:
CREATE DATABASE school;

# Show all databases: 
SHOW DATABASES;

# Use a database:
USE school;


# 2. Table Operations

# Create a table: 
CREATE TABLE STUDENT (
    ROLLNO INT(3) PRIMARY KEY, 
    NAME VARCHAR(15) NOT NULL, 
    PHONE CHAR(10) UNIQUE, 
    AGE INT(2) DEFAULT 16, 
    CITY VARCHAR(15), 
    PERCENTAGE FLOAT(5,2), 
    CHECK (AGE >= 16)
);

# Show all tables:
SHOW TABLES;

# Describe table structure: 
DESC STUDENT;

# Rename a table: 
ALTER TABLE STUDENT RENAME TO XII_CS_STUDENTS;


# 3. Alter Table Operations

# Add a column:
ALTER TABLE STUDENT ADD Email VARCHAR(255);

# Remove a column:
ALTER TABLE STUDENT DROP COLUMN Email;

# Modify column datatype & size:
ALTER TABLE STUDENT MODIFY ROLLNO CHAR(5);

# Remove primary key:
ALTER TABLE STUDENT DROP PRIMARY KEY;

# Add primary key:
ALTER TABLE STUDENT ADD PRIMARY KEY (ROLLNO);

# Rename a column:
ALTER TABLE STUDENT CHANGE ROLLNO RNO INT(3);
