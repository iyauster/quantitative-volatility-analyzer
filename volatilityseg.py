import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_annualized_volatility(ticker: str, start_date: str, end_date: str) -> float:
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    if data.empty:
        raise ValueError(f"No data found for ticker {ticker} in the given date range.")
    
    data['log_returns'] = np.log(data['Close'] / data['Close'].shift(1))
    annualized_volatility = data['log_returns'].std() * np.sqrt(252)
    return annualized_volatility

def plot_rolling_volatility(ticker:str, start_date:str, end_date:str, window: int = 30):
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    if data.empty:
        raise ValueError(f"No data found for ticker {ticker} in the given date range.")
    
    data['log_returns'] = np.log(data['Close'] / data['Close'].shift(1))
    rolling_std = data['log_returns'].rolling(window=window).std()
    data['rolling_volatility'] = rolling_std * np.sqrt(252)
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['rolling_volatility'], label=f'{window}-Day Rolling Volatility')
    plt.title(f'Annualized Rolling Volatility for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.legend()
    plt.show()