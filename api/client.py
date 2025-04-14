import requests
from datetime import datetime, timedelta
from pytz import timezone
from utils.logger import setup_logger
from config.settings import API_DOMAIN, API_KEY, API_KEY_HEADER

logger = setup_logger("api_client")

def get_execution_date(dt):
    """Get the execution date based on the provided offset"""
    brazil_tz = timezone('America/Sao_Paulo')
    # Get the current date in Brazil timezone and add the offset
    # dt can be -1 (yesterday), 0 (today), or 1 (tomorrow)
    return (datetime.now(brazil_tz) + timedelta(days=dt)).strftime("%Y-%m-%d")

def fetch_data(dt):
    """Fetch data from the scrape endpoint using the provided date"""
    execution_date = get_execution_date(dt)
    endpoint = f"{API_DOMAIN}/scrape/{execution_date}"
    
    logger.info(f"Fetching data...")
    
    try:
        headers = {API_KEY_HEADER:API_KEY}
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Raise exception for 4XX/5XX responses
        
        data = response.json()
        logger.info(f"Successfully fetched {len(data)} records")
        return data
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data: {e}")
        return None