
+<h3>Data types:</h3>
	-TEXT
	-CHARACTER
	-VARCHAR(size)
	-INTEGER
	-REAL
	-FLOAT
	-DOUBLE
	-DATE (2019-03-08)
	-DATETIME (2019-03-08 18:39:38)
	-BOOLEAN

+<h3>Constrains:</h3>	
	-NOT NULL
	-CHECK
	-primary key
	-default
	-unique

+<h3>Commands:</h3>
	-.tables
	-.mode column
	-.mode csv
	-.headers on
	-.width
	-.exit
	-.schema
	-.show
	-.output
	-.dump

sqlite3 database.db


create table tname(id ineteger primary key,
name text);
insert into tname values(1,"majed");
insert into tname(name) values("majed2");
drop table tname;


