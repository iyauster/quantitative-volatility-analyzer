from volatilityseg import calculate_annualized_volatility, plot_rolling_volatility
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command line tool to analyze historical volatility of a stock.")
    parser.add_argument('ticker' , metavar = "ticker", help='Stock ticker symbol (Ex: AAPL)')
    parser.add_argument('start_date' , metavar= 'start_date', help='Start Date in YYYY - MM -DD')
    parser.add_argument('end_date' , metavar= 'end_date', help='End Date in YYYY - MM -DD')
    parser.add_argument("-p", "--plot", action="store_true", help="Display a plot of rolling volatility instead of a single value.")
    args = parser.parse_args()
    try:
        if args.plot:
            print(f'Generating a plot for {args.ticker}:')
            plot_rolling_volatility(args.ticker, args.start_date, args.end_date)
        else:
            vol = calculate_annualized_volatility(args.ticker, args.start_date, args.end_date)
            print(f"Annualized Volatility for {args.ticker} from {args.start_date} to {args.end_date}: {vol:.2%}")
    except Exception as e:
        print(f"An error occurred: {e}")

