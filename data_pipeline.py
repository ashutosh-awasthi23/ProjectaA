print("Sanity Check: The script is successfully running!")

import yfinance as yf

def get_live_stock_price(ticker_symbol):
    print(f"Connecting to market data for :")

    stock = yf.Ticker(ticker_symbol) ## Ticker Object Creation
    try:
        ## Fetching the current live price using fast_info
        current_price = stock.fast_info['lastPrice']
        company_name = stock.info.get("shortName",ticker_symbol)
        print(f"Sucess ! {company_name}({ticker_symbol}) is currently trading at : ${current_price :.2f}")
    except Exception as e:
        print(f"Error fetching data for {ticker_symbol}.Error details: {e}")

if __name__ == "__main__":
    ## Testing with apple 
    get_live_stock_price("AAPL")