import requests
from db_utils import create_db_engine, insert_into_db
from schema_mappings import map_dividends_data, map_delisted_data
from models import dividends_table, delisted_companies_table
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exists, insert
import concurrent.futures
from tqdm import tqdm


# # Constants
API_KEY = 'o4xZcqagSkwdrCt5080GWzZKFo9gyucJ'
DELISTED_URL_TEMPLATE = "https://financialmodelingprep.com/api/v3/delisted-companies?page={}&apikey={}"
DIVIDEND_URL_TEMPLATE = "https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/{}?apikey={}"
DB_CONNECTION = "postgresql+psycopg2://postgres:postgres@postgres-data/financial"

# Create a database engine
engine = create_db_engine(DB_CONNECTION)
Session = sessionmaker(bind=engine)


# Function to fetch data from API
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle errors (e.g., logging, raise exception)
        pass


def is_duplicate(symbol, session):
    return session.query(exists().where(delisted_companies_table.c.symbol == symbol)).scalar()


def fetch_and_process_delisted():
    page_num = 0
    while True:
        with Session() as session:
            delisted_data = fetch_data(
                DELISTED_URL_TEMPLATE.format(page_num, API_KEY))
            if not delisted_data:  # Stop if there's no data
                break

            new_records = [record for record in delisted_data if not is_duplicate(
                record['symbol'], session)]

            if not new_records:  # Stop if all records are duplicates
                break

            # print(page_num)
            session.execute(
                insert(delisted_companies_table),
                new_records
            )
            session.commit()

            page_num += 1


def fetch_dividends(symbol):
    url = DIVIDEND_URL_TEMPLATE.format(symbol, API_KEY)
    dividends_data = fetch_data(url)
    if dividends_data and 'historical' in dividends_data:
        print(symbol)
        dividends_df = map_dividends_data(dividends_data)
        insert_into_db(dividends_df, dividends_table, engine)


def process_dividends_data():
    with Session() as session:
        symbols_list = session.query(delisted_companies_table.c.symbol).all()
        symbols = [symbol[0] for symbol in symbols_list]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        list(tqdm(executor.map(fetch_dividends, symbols), total=len(symbols)))


def main():
    # Fetch and process delisted companies data
    fetch_and_process_delisted()

    # Fetch and process dividends data
    process_dividends_data()


if __name__ == "__main__":
    main()
