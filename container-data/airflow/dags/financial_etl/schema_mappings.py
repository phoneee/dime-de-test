import pandas as pd

def map_dividends_data(data):
    dividends_company = [{
        'symbol': data['symbol'],
        'date': row['date'],
        'label': row['label'],
        'adjDividend': float(row['adjDividend']),
        'dividend': float(row['dividend']),
        'recordDate': row['recordDate'],
        'paymentDate': row['paymentDate'],
        'declarationDate': row['declarationDate']
    } for row in data['historical']]
    df = pd.DataFrame(dividends_company)

    # Convert date columns to datetime format
    date_columns = ['date', 'recordDate', 'paymentDate', 'declarationDate']
    for col in date_columns:
        df[col] = pd.to_datetime(df[col])

    return df


def map_delisted_data(data):
    df = pd.DataFrame(data)
    df['ipoDate'] = pd.to_datetime(df['ipoDate'])
    df['delistedDate'] = pd.to_datetime(df['delistedDate'])
    return df
