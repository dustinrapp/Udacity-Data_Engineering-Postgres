#### TEST

Do the following steps in your README.md file.
Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
How to run the Python scripts
An explanation of the files in the repository
State and justify your database schema design and ETL pipeline.

# Introduction
Client would like assistance with analyzing collected song and user activity data which was collected using their new music streaming app.  They would like to better understand the songs their listeners are streaming. In order to perform this analysis, they first need a database which recievies streaming song/user information. Data logs are in JSON format. Once this data is in a database, informative queries can be made to analyze the data.  The client requests that a database schema and ETL pipeline be creaated.  This report documents this creation.

# Process
In order to implement this database and ETL pipeline, the following steps are taken:
1.) Define fact and dimensition tables for the star schema
2.) Create postgres database database and applicable tables
3.) Load song/user data into tables
4.) Query data to confirm accuracy

The client provided two datasets*..  The first was for the song data, containing metatdata in JSON format for songs played at their site.  The second was a log file, containing information about each play at their site (e.g. user, song played, metadata about connection, time played, etc.).  

*Note: Both of these are fictious datasets.  The first dataset contains real data from the Million Song Dataset (1) and was provided by Udacity.  The second dataset was log data simulated by an event simulator (2) using data generated the first dataset, and was also supplied by Udacity for this exercise.  These data files were also in JSON format** 


# Fact/Dimension Tables
Utilizing the song data and log datasets, a star schema database was created as follows:

### Fact Table
+ songplays - this contains song play log data (i.e. records with page NextSong)
    ++ Columns: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
### Dimension Tables
+ users - users in the app
+ user_id, first_name, last_name, gender, level
+ songs - songs in music database
+ song_id, title, artist_id, year, duration
+ artists - artists in music database
+ artist_id, name, location, latitude, longitude
+ time - timestamps of records in songplays broken down into specific units
+ start_time, hour, day, week, month, year, weekday


"A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.""

Project Description
"In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL."

### Methodology

Fact and dimension tables were created in *create_tables.py*
Data was extracted from the song data and log data files (found in data folder) and inserted into approprate database tables using *etl.py*. Finally testing of the database is found in test.pynb

Footnotes
*This is a fictious dataset which contains subset of real data from the Million Song Dataset (1) and was provided by Udacity. 

### References
Thierry Bertin-Mahieux, Daniel P.W. Ellis, Brian Whitman, and Paul Lamere. 
The Million Song Dataset. In Proceedings of the 12th International Society
for Music Information Retrieval Conference (ISMIR 2011), 2011.

https://github.com/Interana/eventsim
