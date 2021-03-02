# DB-Table-Data-Transporter
-Designed for Copying a Table from MySQL DB , into PostgreSQL DB.

-FLASK Project

- Takes inputs( USER,PASSWORD,DATABASE NAME, HOST IP ) for both MySQL and PostgreSQL Database
- Lists All Table from MySQL DB
- Request a table name to copy into PostgreSQL,from user.
- Creates a table into PostgreSQL DB with selected table name.
- (!!!DROPS table if there is table with same namee ,so check your PostgreSQL DB before!!!)
- Copies MySQL table columns and datas into new created table in PostgreSQL.
- Displays a message for succeed process.


Tested with localhost server (with varchar,int column type and default schema)


![1](https://user-images.githubusercontent.com/62523196/109721919-0b16a180-7bbd-11eb-94bc-95684730733e.PNG)

![2](https://user-images.githubusercontent.com/62523196/109721953-1669cd00-7bbd-11eb-9021-b3c0c3b92138.PNG)

![3](https://user-images.githubusercontent.com/62523196/109721963-1b2e8100-7bbd-11eb-982b-6e0f6afdd830.PNG)

ENG[3rd Image]: Selected table -tablenamefromMySQL- from (MySQL) succesfully copied into -PostgreSQL_DatabaseNAME-.
