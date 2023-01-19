import pandas as pd
import pandas_ta as ta
import warnings

def calculate_indicators(file_name):
    # Read the CSV file and create a pandas dataframe
    df = pd.read_csv(file_name, sep=',')

    # Calculate the indicators using the pandas-ta library
    #df.set_index(pd.DatetimeIndex(df['Date']), inplace=True)
    df['short_ma'] = ta.sma(df['Close'], length=50)
    df['long_ma'] = ta.sma(df['Close'], length=200)
    df['rsi'] = ta.rsi(df['Close'], n=8)

    warnings.filterwarnings("ignore", category=FutureWarning)
    macd = ta.macd(df['Close'])
    df['macd'] = macd['MACD_12_26_9']
    df['macd_hist'] = macd['MACDh_12_26_9']
    df['macd_signal'] = macd['MACDs_12_26_9']

    df['Close_shift'] = df['Close'].shift(-1)

    # Create a new column that is the percentage change between the original 'Close' column and the shifted 'Close' column
    df['Close_pct_change'] = (df['Close_shift'] / df['Close']) - 1
    df.drop(columns='Close_shift', inplace=True)

    df['Close_pct_change'] = df['Close_pct_change'] * 100
    df['Close_pct_change'] = round(df['Close_pct_change'])

    # Round all data to 2 decimal places
    df = round(df, 2)


    # Write the updated data back to the CSV file
    df.to_csv(file_name, index = False)

# Example usage
calculate_indicators('NAS.csv')