## 0x0D. SQL - Introduction
## In this project I have learned about:
    * What’s a database
    * What’s a relational database
    * What does SQL stand for
    * What’s MySQL
    * How to create a database in MySQL
    * What does DDL and DML stand for
    * How to CREATE or ALTER a table
    * How to SELECT data from a table
    * How to INSERT, UPDATE or DELETE data
    * What are subqueries
    * How to use MySQL functions
## Tasks                                                                                                   
    0-Write a script that lists all databases of your MySQL server                            
    1-Write a script that creates the database hbtn_0c_0 in your MySQL server                 
    2-Write a script that deletes the database hbtn_0c_0 in your MySQL server                  
    3-Write a script that lists all the tables of a database in your MySQL server.             
    4-Write a script that creates a table called first_table in the current database      
       in your MySQL server.
        first_table description:
         * id INT
         * name VARCHAR(256)

    5-Write a script that prints the full description of the table first_table                  
       from the database hbtn_0c_0 in your MySQL server.
    6-Write a script that lists all rows of the table first_table from the database hbtn_0c_0 
    7-Write a script that inserts a new row in the table first_table (database hbtn_0c_0)      
        New row:
         * id = 89
         * name = Best School

    8-Write a script that displays the number of records with id = 89                           
       in the table first_table of the database hbtn_0c_0
    9-Write a script that creates a table second_table in the database hbtn_0c_0              
      second_table description:
       * id INT
       * name VARCHAR(256)
       * score INT
 
    10-Write a script that lists all records of the table                                       
       second_table of the database hbtn_0c_0
    11-Write a script that lists all records with a score >= 10                                
    12-Write a script that updates the score of Bob to 10 in the table second_table            
    13-Write a script that removes all records with a score <= 5 in the table second_table     
    14-Write a script that computes the score average of all records in the table second_table 
    15-Write a script that lists the number of records with the same score                     
       in the table second_table of the database hbtn_0c_0
        The result should display:
          the score
          the number of records for this score with the label number
          The list should be sorted by the number of records (descending)
          The database name will be passed as an argument to the mysql command

    16-Write a script that lists all records of the table second_table                        
       Don’t list rows without a name value
       Results should display the score and the name (in this order)
       Records should be listed by descending score 
       The database name will be passed as an argument to the mysql command
## File
    0-list_databases.sql
    1-create_database_if_missing.sql
    2-remove_database.s
    3-list_tables.sql
    4-first_table.sql
    5-full_table.sql
    6-list_values.sql
    7-insert_value.sql
    8-count_89.sql
    9-full_creation.sql
    10-top_score.sql
    11-best_score.sql
    12-no_cheating.sql
    13-change_class.sql
    14-average.sql
    15-groups.sql
    16-no_link.sql
