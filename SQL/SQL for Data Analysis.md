SQL is the language used to communicate with databases. 

SQL is used to access, manipulate, and retrieve data from objects in a database. 

Databases can have one or more schemas, which provide the organization and structure and contain other objects.

Within a schema, the objects most commonly used in data analysis are tables, views, and functions.

Tables contain fields, which hold the data. 
  Tables may have one or more indexes; an index is a special kind of data structure that allows data to be retrieved more efficiently. 
  Views are essentially stored queries that can be referenced in the same way as a table. 
  Functions allow commonly used sets of calculations or procedures to be stored and easily referenced in queries. 
  
![Overview_of_DB_and_Objects](https://user-images.githubusercontent.com/16577898/206371691-ef43a1ea-026b-450f-afda-88f41d88b3ae.jpg)

DQL, or data query language - It’s used for querying data, which you can think of as using code to ask questions of a database. DQL commands include SELECT.

DDL, or data definition language - is used to create and modify tables, views, users, and other objects in the database. It affects the structure but not the contents. There are three common commands: CREATE, ALTER, and DROP.

DCL, or data control language, is used for access control. Commands include GRANT and REVOKE.

DML, or data manipulation language, is used to act on the data itself. The commands are INSERT, UPDATE, and DELETE.

Database Types
  1. Row-store databases—also called transactional databases - are designed to be efficient at processing transactions: INSERTs, UPDATEs, and DELETEs. Example: Postgres.
  2. 
