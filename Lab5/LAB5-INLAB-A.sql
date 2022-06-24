-- SQLite
 CREATE TABLE Student2(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50));

INSERT INTO Student2 (ID, NAME, AGE, ADDRESS)
VALUES (1, 'Errol', 19,'San manuel');

SELECT* FROM EnrolledDB;