/*
indentation doesn't matter; can write sql code in one line
however, best leave one line for each part to make code more readable

separate distinct code using ; if run together

for example:
CREATE TABLE FirstTable (Column DataType);

CREATE TABLE SecondTable (Column DataType) 
*/

/* 
using db browser for sqlite
VERY IMPORTANT: WRITE CHANGES: save changes, such as creation of tables
revert changes: undo changes  

type code in execute sql box then press single rightward arrow to execute all sql statements 
*/



-- operations to structure of database


/*
create table 
usually copy code from create table under database structure in db browser for sqlite cause sql hardly tested alone
*/

CREATE TABLE table_name(
column1_name COLUMN1_TYPE COLUMN1_CONSTRAINTS,
column2_name COLUMN2_TYPE COLUMN2_CONSTRAINTS,
PRIMARY KEY (column1_name, column2_name),
FOREIGN KEY (column_name) REFERENCES table2_name(column_name)
); 
-- foreign key links primary key to another table's primary key 


/* 
alter table 
operate (add/ delete/ modify) column in existing table 
change (add/ drop) constraints of existing table 
*/ 

-- add new column 
ALTER Table table_name ADD new_column_name TEXT 
-- replace TEXT with appropriate data type (INTEGER, etc)

-- existing table 
ALTER TABLE old_table_name RENAME TO new_table_name 
-- modify (change name) table 


/* 
drop table 
remove table from existence
no more entries can be inserted into table after getting dropped 
*/

DROP TABLE table_name 



--dealing with data: 

/*
data types (for db browser for sqlite):
INTEGER -> whole numbers
TEXT -> python string 
BLOB -> binary data, such as images
REAL -> float (8 bit)
NUMERIC -> mix of integer and real. tries to store as integer first, if that fails then store as real  

tips:
store dates as integer in format YYYYMMDD  
so that easier to sort (by year then month then day) and query (dates in a specific year)

store values that can start with zero as text  

constraints (symbol in db browser for sqlite): 
not null (No) -> requires field to be filled
primary key (PK) -> refer to database notes 
auto increment(AI) -> assign numbers in ascending order (2 after 1, etc) 
unique (U) -> field's value is unique | auto enforced for primary keys  
foreign key (Foreign Key) -> double click to set, second option is column in other table   
check (Check) -> validate format 
*/

/*
querying data:

structure of query:
SELECT (choose columns)
FROM (choose table)
JOIN ON (only required when joining another table, refer below for different joins)
WHERE (filter records)
GROUP BY (group records)
HAVING (filter groups)
ORDER BY (sort output)

 
operators (comparison, logical, arithmetic;math)
most often used in select but can be used in other statements

comparison: 
= ->
!= ->
<> ->
> ->
< ->
>= ->
<= ->

logical:
AND, OR -> python logic, in WHERE clause 
IS -> check for existence of value  
ISNOT -> check for no existence of value 
|| -> string concatenation 

arithmetic:
+ -> addition
- -> subtraction 
* -> multiplication 
/ -> division
% -> modulus; remainder when left hand side divided by right hand side 
*/ 


-- data manipulation language (select/ insert/ update/ delete)

-- select 

-- using only one table 
SELECT column1_name, column2_name 
FROM table_name
WHERE column3_name = condition1 AND column4_name = condition2 
ORDER BY column1_name ASC 

/* 
SELECT * for all columns from table

default for ORDER BY is ascending order (ASC) if ASC/DESC not specified
use DESC to order in descending order 
*/


/* 
aggregate functions 
MIN(), MAX(), SUM(), COUNT() 
used with group by statement to group result by columns 
*/

-- example: find publisher who published the most books  
SELECT PublisherID, COUNT(PublisherID) AS BooksPublished
FROM Book 
GROUP BY PublisherID 
ORDER BY BooksPublished DESC
LIMIT 1;


-- update 

UPDATE table_name 
SET column_name = "new_data" 
WHERE column_name = condition 

/*
SET column_name = 'new_data' || column_name 
remove WHERE when updating all data in column 
*/  


/*
insert 
NOTE: syntax here differs slightly from sqlite3; cannot fully copy insert sql code into sqlite3
check if inserted correctly by looking at table under "Browse Data" in db browser for sqlite 
*/

INSERT INTO table_name(column1_name, column2_name)
VALUES ("data1","data2")


-- delete 

DELETE FROM table_name 
WHERE column_name = "delete_data"
-- WHERE condition don't have to equal, can be a range such as < value

/*
remove WHERE condition to delete all entries from table
different from DROP as table still present; don't have to recreate table
*/


/* 
two tables

condition (WHERE/ON) matches data according to common column (foreign key)
use table_name.column to specify column of which table 
using alias keyword: SELECT something AS keyword, useful if lazy type out long names 
*/


-- different joins 

/*
cross join (most useless) 
combines every row in first table with every row in second table   
in math terms: union of both tables; table1 ∪ table2
*/

SELECT * 
FROM table1_name, table2_name 


/*
inner join (default)
for data that appear in both tables matching condition 
in math terms: intersection of both tables; table1 ∩ table2
*/

SELECT *
FROM table1_name
INNER JOIN table2_name 
ON table1_name.column_name = table2_name.column_name 
-- ON is condition


/*
left outer join (include everything from left (first table) )
all from first table and those from second table matching condition 
useful if got desired data from first table that don't meet condition 
vice versa for right outer join 
*/

SELECT *
FROM table1_name
LEFT OUTER JOIN table2_name
ON table1_name.column_name = table2_name.column_name 


/*
nested/subquery 
required if need use data from one table to query from another table 
essentially two queries together 
*/

-- most common usage: SELECT statements 
-- example: get names of customers who have purchased more than $50 (assuming purchase amount adds up after each transaction) 
SELECT Name 
FROM Customer
WHERE CustomerID = (
SELECT CustomerID 
FROM Records  
WHERE PurchaseAmount > 50)

-- insert from another table by replacing VALUES () with appropriate SELECT statements
-- example: 
INSERT INTO ArchivedMembers (MemberID, FirstName, LastName, Email)
SELECT MemberID, FirstName, LastName, Email
FROM Member
WHERE LastActivityDate < "2022-01-01"


-- example of everything combined: find borrowers who have borrowed more than 3 books written by John
SELECT Borrower.Name, COUNT(Loan.LoanID) AS BooksBorrowed
FROM Borrower 
INNER JOIN Loan ON Borrower.BorrowerID = Loan.BorrowerID
WHERE Loan.AuthorName = "John"
GROUP BY Borrower.BorrowerID, Borrower.Name
HAVING COUNT(Loan.LoanID) > 3
ORDER BY BooksBorrowed DESC