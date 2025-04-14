import psycopg2
from psycopg2.extras import execute_values
from utils.logger import setup_logger
from config.settings import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT, TABLE_NAME, SSLMODE

logger = setup_logger("db_handler")

def get_connection():
    """Create and return a database connection"""
    DB_CONFIG = {
        "dbname": DB_NAME,
        "user": DB_USER,
        "password": DB_PASSWORD,
        "host": DB_HOST,
        "port": DB_PORT,
        "sslmode": SSLMODE
    }
    return psycopg2.connect(**DB_CONFIG)

def insert_data(data):
    """Insert the fetched data into PostgreSQL database"""
    if not data or len(data) == 0:
        logger.warning("No data to insert")
        return
    
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Extract column names from the first dictionary
        columns = list(data[0].keys())
        
        # Create a list of tuples for values
        values = [[item[column] for column in columns] for item in data]
        
        # Construct the SQL query
        insert_query = f"""
        INSERT INTO {TABLE_NAME} ({', '.join(columns)})
        VALUES %s
        ON CONFLICT (game_id) 
        DO UPDATE SET 
            home_team_score = EXCLUDED.home_team_score,
            away_team_score = EXCLUDED.away_team_score
        """
        
        # Execute the query with all the data
        execute_values(cursor, insert_query, values)
        
        # Commit the transaction
        conn.commit()
        logger.info(f"Successfully inserted {len(data)} rows into {TABLE_NAME}")
        return True
        
    except Exception as e:
        logger.error(f"Database error: {e}")
        if conn:
            conn.rollback()
        return False
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()