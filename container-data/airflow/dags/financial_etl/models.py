from sqlalchemy import Table, Column, String, MetaData, Float, Date, Text

metadata = MetaData()

dividends_table = Table(
    'dividends_table', metadata,
    Column('symbol', String, nullable=False),
    Column('date', Date, nullable=False),
    Column('label', String, nullable=False),
    Column('adjDividend', Float, nullable=False),
    Column('dividend', Float, nullable=False),
    Column('recordDate', Date, nullable=True),
    Column('paymentDate', Date, nullable=True),
    Column('declarationDate', Date, nullable=True)
)

delisted_companies_table = Table(
    'delisted_companies_table', metadata,
    Column('symbol', String, nullable=False, primary_key=True),
    # Using Text for potentially longer company names
    Column('companyName', Text, nullable=True),
    Column('exchange', String, nullable=False),
    Column('ipoDate', Date, nullable=False),
    Column('delistedDate', Date, nullable=False)
)
