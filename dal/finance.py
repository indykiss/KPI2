
# Data access layer. Facade for yf
import yfinance as yf

def get_data(symbol, start_date, end_date):
    ticker = yf.Ticker(symbol)
    result = ticker.history(start=start_date, end=end_date)
    return result 

def get_ticker(symbol):
    return yf.Ticker(symbol)


# idk lots to do here 
def get_yf_ticker(ticker, start_date, end_date):
    if ticker == '':
        return 'Please Enter a Stock Ticker'
    else: 
        # stockFormat, symbol = verify_ticker(ticker)
        stock = yf.Ticker(symbol)
        result = ticker.history(start=start_date, end=end_date)
            