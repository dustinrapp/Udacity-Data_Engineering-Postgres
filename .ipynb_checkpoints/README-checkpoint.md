
# Introduction
A client (Sparkify) would like assistance with analyzing collected song and user activity data which was collected using their new music streaming app.  They would like to better understand the songs their listeners are streaming. In order to perform this analysis, they first need a Postgres database which recievies streaming song/user information. Data logs are in JSON format. Once this data is in a database, informative queries can be made to analyze the data.  The client requests that a database schema and ETL pipeline be creaated.  This github repository provides data and scripts used to create the needed database, ETL processing, and testing. 

# Process
In order to implement this database and ETL pipeline, the following steps are taken:  

1.) Obtain song and user data  
2.) Define fact and dimensition tables for the star schema  
2.) Create postgres database database and applicable tables  
3.) Load song/user data into tables  
4.) Query data to confirm accuracy  

# Obtaining Data
The data for to test and demonstrate this particular project was provided by Udacity, and are found in the data folder. Two sets of data were provided:

**Song Dataset**: This datasets is associated with Thierry B, et al. 2011 and can be found on http://millionsongdataset.com/.  The data contained songs Sparkify might play, as well as artist/song metadata in JSON format. This dataset contained info on ___ songs.

**Log Dataset**:  This dataset is generated by *eventsim* (https://github.com/Interana/eventsim), which is an application that simulates music streaming app activity logs.  There are two files in the dataset - one for 11/12/2018, and one for 11/13/2018. Each contain activity logs in JSON format and contain such information such as the name, gener, location, song listened to, time listenting and userid of the streaming service.  These activity logs are intended to simulate activity logs which would be generated by Songify's app.


# Defining the Data Model Star Schema
Before creating the database, the Data Model was considered.  A Star Schema model was chosen for its simplicity.  Recall a Fact table narrows down the facts (measurements, metrics, etc) needed for the business problem at hand. The dimension tables  help categorize the facts and measures found in the fact table. Descriptions of the Fact and Dimension Tables which form the database are described below:

### Fact Table
1.) **songplays** - this contains song play log data (i.e. records with page NextSong) in the following fields: 
* Songplay_id: unique id of the records song play
* start_time: start time of the song play
* user_id: unique id of the person initiating the song play
* level: the user membership level
* song_id: unique id associated with the song the song played
* artist id:  unique id of artist played, the session id, as well as location of the ply.
* session_id: unique id associated with the session in which the song play occurred
* user_agent: metadata information on the agent that the user played the song (e.g. web browser, operating system, etc)

 
### Dimension Tables
1.) **users** - contains app user information in the following fields:
* user_id - unique id of the user
* first_name - first name of user
* last_name - last name of user
* gender - gender of user
* level - level of membership of user  

2.) **songs** - contains info on all songs in their music database in the following fields:  
* song_id
* title
* artist_id
* year
* duration  

3.) **artists** - contains info on all artists in their music database in the following fields:
* artist_id  
* name
* location
* latitude
* longitude

4.) **time** - contains timestamp of the records found in the **songplays** table, broken down into specific units as fields:
* start_time
* hour 
* day
* week
* month
* year
* weekday*

## Database Creation   
The database was created using the Python library psycopg2 in conjunction with a Postgresql database connection. The code which creates the necessary database and Fact/Dimension tables is found in *create_tables.py* script. The *sql_queries.py* script was utilized as a library of queries for the *create_tables.py* to utilize.


## Loading Data
Once the appropriate tables were created in the database, data in the song dataset was loaded into the tables.  This was performed using the *etl.py* script.The *sql_queries.py* script was also utilized as a library of queries for the *etl.py* script to utilize.

  
## Testing/Verifying Test
Several sql queries were performed to verify script performance.  These test were run within *test.ipynb*.  

## Running Scripts  
To run the scripts, download the github repsository (including data files) to your local computer.   Once there, run *create_tables.py* from a command prompt. This python script accepts four arguments from the command line - the host ip address, the server it is to connect to, as well as username and password to access the respective server (in that order).  For example: *create_tables.py 127.0.0.1 Udacity_Postgre postgres password* This will connect to the Udacity_Postgres_Database and create a new *sparkifydb* database with the needed Fact and Dimension tables.  Note if a sparkifydb database already exists, it will be removed and a new sparkifydb database created.

Once the *sparkify* database is created with needed tables, the *etl.py* script must also be run from the command line. This script will pull data from the log and song datafiles and insert them into the *sparkify* tables.  The data to be read must be in a data folder in the working directory.  This python script also accepts four arguments from the command line - the host ip address, the database it is to connect to and insert data into, as well as username and password to access the respective database (in that order).  For example: *etl.py 127.0.0.1 sparkify postgres password*.
    


**REFERENCES**
Thierry Bertin-Mahieux, Daniel P.W. Ellis, Brian Whitman, and Paul Lamere. 
The Million Song Dataset. In Proceedings of the 12th International Society
for Music Information Retrieval Conference (ISMIR 2011), 2011