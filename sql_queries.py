## This script contains commonaly used variables in the etl.py and create_tables.py script.  It is broken into sections:
#'CREATE/DROP TABLES' sections - Utilized by the create_database function in create_tables.py during table creation. 
# 'INSERT RECORDS' section - Utilized to insert data from files into respective tables during the ETL phase.  These are used in the 'process_log_file' and 'process_song_file' in the etl.py script. 

#CREATE/DROP TABLES


# Drop table queries
songplay_table_drop = "DROP TABLE IF EXISTS songs"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# Create Table Queries
songplay_table_create = "CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY, start_time timestamp NOT NULL, user_id int NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar);"
#songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

user_table_create = "CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level varchar);"

song_table_create = "CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar, artist_id varchar, year int, duration numeric(9,5));"

artist_table_create = "CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, name varchar NOT NULL, location varchar, latitude double precision, longitude double precision);"

time_table_create = "CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour int, day int, week int, month int, year int, weekday int);"

#Lists of all create and drop table queries. Used so scripts can loop through all queries.
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]


# INSERT RECORDS
songplay_table_insert =  "INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s) \
 ON CONFLICT DO NOTHING"

user_table_insert = "INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) \
ON CONFLICT (user_id) DO NOTHING"

song_table_insert = "INSERT INTO songs (song_id, title, artist_id, year, duration)  VALUES (%s, %s, %s, %s, %s) \
ON CONFLICT (song_id) DO NOTHING"

artist_table_insert ="INSERT INTO artists (artist_id, name, location, latitude, longitude)  VALUES (%s, %s, %s, %s, %s) \
ON CONFLICT (artist_id) DO NOTHING"


time_table_insert = "INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)"

# song_select is used to select needed song and artist information from both the song_id and artist_id table table for insertion into the songplays table
song_select = "SELECT songs.song_id, artists.artist_id, songs.duration FROM (artists JOIN songs on artists.artist_id = songs.artist_id) WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s"
