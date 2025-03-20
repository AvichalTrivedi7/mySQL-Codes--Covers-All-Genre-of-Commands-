# 7. Handling NULL Values

# Show students where phone number is missing: 
SELECT * FROM STUDENT WHERE PHONE IS NULL;

# Show students who have provided a phone number:
SELECT * FROM STUDENT WHERE PHONE IS NOT NULL;


# 8. Sorting and Grouping

# Sort names in ascending order: 
SELECT NAME FROM STUDENT ORDER BY NAME;

# Sort names in descending order:
SELECT NAME FROM STUDENT ORDER BY NAME DESC;

# Group by city (number of students in each city): 
SELECT CITY, COUNT(CITY) FROM STUDENT GROUP BY CITY;

# Filter grouped results using HAVING:
SELECT CITY, COUNT(CITY) FROM STUDENT GROUP BY CITY HAVING CITY = 'JODHPUR';


# 9. Aggregate Functions

# Total percentage of students in each city:
SELECT CITY, SUM(PERCENTAGE) FROM STUDENT GROUP BY CITY;

# Average percentage of students in each city:
SELECT CITY, AVG(PERCENTAGE) FROM STUDENT GROUP BY CITY;

# Minimum percentage of students:
SELECT CITY, MIN(PERCENTAGE) FROM STUDENT;

# Maximum percentage of students:
SELECT CITY, MAX(PERCENTAGE) FROM STUDENT;

# Count students in each city:
SELECT CITY, COUNT(CITY) FROM STUDENT GROUP BY CITY;