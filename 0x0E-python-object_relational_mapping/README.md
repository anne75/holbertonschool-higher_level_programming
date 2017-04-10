## MySQLdb & sqlAlchemy

##### Introduction
Connecting python with a mysql database.  
For this project, we used 2 ways to connect to query a MySQL database from a python script.  
First we used the `MySQLdb` module and wrote SQL statements.  
Then we used the `sqlachemy` ORM module and only used a more pythonic object notation.  

#### Installing the packages
- `MySQLdb`  
```sudo apt-get install python3-dev   
sudo apt-get install libmysqlclient-dev   
pip3 install mysqlclient
```   
- `sqlAlchemy`  
`pip3 install SQLAlchemy`   

#### MySQLdb
With this module, we write SQL queries as strings and python pass them along to the database.

#### sqlAlchemy
With this module, we use Object Relational Mapping. So we create classes that match SQL tables. We then run queries on the database, but using an  "object notation".
