import yfinance as yf
import pandas as pd
import numpy as np

ticker = 'SPY'
start_date = '2020-01-01'
end_date = '2025-10-13'
data = yf.download(ticker, start=start_date, end=end_date)

data['log_returns'] = np.log(data['Close'] / data['Close'].shift(1))
annualized_volatility = data['log_returns'].std() * np.sqrt(252)
print(f"Annualized Volatility for {ticker} from {start_date} to {end_date}: {annualized_volatility:.2%}")
