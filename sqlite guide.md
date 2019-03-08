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



</ul>
sqlite3 database.db


create table tname(id ineteger primary key,
name text);
insert into tname values(1,"majed");
insert into tname(name) values("majed2");
drop table tname;


