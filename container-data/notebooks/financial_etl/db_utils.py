# db_utils.py

from sqlalchemy import create_engine, Table, select
from models import metadata


def create_db_engine(db_connection_string):
    engine = create_engine(db_connection_string)
    metadata.create_all(engine)
    return engine


def insert_into_db(df, table, engine):
    with engine.connect() as conn:
        for _, row in df.iterrows():
            # Check if the record already exists
            exists_query = select([table]).where(
                table.c.symbol == row['symbol'] and
                table.c.date == row['date']
            )
            result = conn.execute(exists_query).fetchone()

            if not result:
                # Record does not exist, insert new record
                insert_query = table.insert().values(row)
                conn.execute(insert_query)


# def insert_new_records(symbol, table, session):
#     new_records = []
#     for record in dividends_data['historical']:
#         record['symbol'] = symbol  # Add symbol to each record
#         if not session.query(table).filter(table.c.symbol == symbol, table.c.date == record['date']).first():
#             new_records.append(record)

#     if new_records:
#         session.execute(insert(table), new_records)
#         session.commit()
