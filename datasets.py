import pandas as pd

def load_data(train_csv, test_csv):

    # Read data into a dataframe
    tdf = pd.read_csv(train_csv)
    df = pd.read_csv(test_csv)

    # Build train and test data sets
    train_x = tdf.drop(columns='Close_pct_change')
    train_y = tdf["Close_pct_change"]
    test_x = df.drop(columns='Close_pct_change')
    test_y = df["Close_pct_change"]




    return train_x,train_y,test_x,test_y


# Debugging
#train_x,train_y,test_x,test_y = load_data('AAPL.csv','LMT.csv')
#
#print(train_x.shape)
#print(train_y.shape)
#print(test_y.shape)
#print(test_x.shape)