import sys

def data():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    return COMPANIES, STOCKS

def get_key(my_dict, val):
    for key, value in my_dict.items():
         if val == value:
             return key

def ticker_symbols():
    if len(sys.argv) != 2:
        return
    val = sys.argv[1].upper()
    COMPANIES, STOCKS = data()
    if val in STOCKS:
        print(get_key(COMPANIES, val), STOCKS[val])
    else:
        print("Unknown ticker")

if __name__ == '__main__':
    ticker_symbols()