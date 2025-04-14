from api.client import fetch_data
from database.db import insert_data
from utils.logger import setup_logger

logger = setup_logger("main")

def main():
    """Main function to run the scraping job"""
    logger.info("Starting daily scraping job")
    
    # Fetch data from the endpoint
    data = []
    for dt in [-1, 0, 1]:
        # Every day fetch data for the last day, today, and the next day
        logger.info(f"Fetching data for date offset: {dt}")
        data.extend(fetch_data(dt=dt))
    
    # Insert data into PostgreSQL if data was fetched successfully
    if data:
        success = insert_data(data)
        if success:
            logger.info("Data successfully processed and stored")
        else:
            logger.error("Failed to store data in database")
    else:
        logger.warning("No data was retrieved from API")
    
    logger.info("Scraping job completed")

if __name__ == "__main__":
    main()