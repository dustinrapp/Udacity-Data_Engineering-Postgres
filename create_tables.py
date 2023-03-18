import psycopg2, sys
from sql_queries import create_table_queries, drop_table_queries


def create_database(host, dbname, user, password):
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    
    # connect to default database
    #conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    default_conn_str = f'host={host} dbname={dbname} user={user} password={password}'
    db_conn_str = f'host={host} dbname=sparkifydb user={user} password={password}'
    
    #conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    
    #Connect to default database
    try:
        print(f'Connecting to database with credentials: {default_conn_str}')
        conn = psycopg2.connect(default_conn_str) 
        conn.set_session(autocommit=True)
        cur = conn.cursor()
    except:
        print('error connecting to default database')
        conn.close()

    
    # Connect to and create sparkify database with UTF8 encoding
    print('Creating new sparkifydb database instance')
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    try:
        print(f'Connecting to sparkify database with credentials: {db_conn_str}')
        conn = psycopg2.connect(db_conn_str)
        cur = conn.cursor()
    except: 
        print('Error connecting to sparkifydb database')
        conn.close()
    
    return cur, conn

def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        print(query)
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    #Make connection to database
    cur, conn = create_database(host = str(sys.argv[1]), 
                                dbname = str(sys.argv[2]),
                                user = str(sys.argv[3]), 
                                password = str(sys.argv[4]))
    
    #Drop applicable tables (if necessary)
    drop_tables(cur, conn)
    
    #Create applicable tables
    create_tables(cur, conn)
    
    #Close database connection
    conn.close()


if __name__ == "__main__":
    
    main()