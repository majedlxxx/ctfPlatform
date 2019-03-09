<ul>
<li>
<h3>Data types:</h3>
<ul>
<li>TEXT</li>
<li>CHARACTER</li>
<li>VARCHAR(size)</li>
<li>INTEGER</li>
<li>REAL</li>
<li>FLOAT</li>
<li>DOUBLE</li>
<li>DATE (2019-03-08)</li>
<li>DATETIME (2019-03-08 18:39:38)</li>
<li>BOOLEAN</li>
</ul>
</li>

<h3>Constrains:</h3>
<ul>
<li>NOT NULL</li>
<li>CHECK</li>
<li>primary key</li>
<li>default</li>
<li>unique</li>
</ul>

<h3>Commands:</h3>
<ul>
<li>.tables</li>
<li>.mode column</li>
<li>.mode csv</li>
<li>.headers on</li>
<li>.width</li>
<li>.exit</li>
<li>.schema</li>
<li>.show</li>
<li>.output</li>
<li>.dump</li>
</ul>



<li>
	<h3>Creating a database file: sqlite3 database.db</h3>
</li>

<li><h3>Creating a table</h3>
<ul><li>create table tableName (<br>
	col_name data_type constrains,<br>
	...<br>
	...<br>
);</li></ul>
</li>

<li><h3>Insert into table</h3>
	<ul>
		<li>insert into tableName values(1,"name");</li>
		<li>insert into tableName("name") values("name");</li>
	</ul>
</li>

<li><h3>Select from table</h3></li>
	<ul>
		<li>select * from tableName;</li>
		<li>select col1, col2 from tableName;</li>
		<li>SELECT col1, col2 FROM tableName WHERE id>5;</li>
		<li>SELECT col1, col2 FROM tableName WHERE name="Name";</li>
	</ul>

<li><h3>Delete from table</h3>
	<ul>
		<li>DELETE FROM tname WHERE id=1;</li>
		<li>DELETE FROM tname WHERE 1=1;</li>
	</ul>
</li>


</ul>