import pandas as pd

# Sample data
trading_data = [
    {
        "amount": 30,
        "profit": 0,
        "status": "CLOSED",
        "type": "SELL",
        "walletType": "DEMO",
        "createdAt": "2023-07-08T11:35:31.000Z",
        "closeOrder": 30204.01,
        "closeResult": 30204.22,
        "pair": "BTC"
    },
    {
        "amount": 20,
        "profit": 39,
        "status": "CLOSED",
        "type": "SELL",
        "walletType": "DEMO",
        "createdAt": "2023-07-08T11:34:16.000Z",
        "closeOrder": 30221.81,
        "closeResult": 30218,
        "pair": "BTC"
    },
    {
        "amount": 20,
        "profit": 0,
        "status": "CLOSED",
        "type": "SELL",
        "walletType": "DEMO",
        "createdAt": "2023-07-08T11:33:25.000Z",
        "closeOrder": 30216,
        "closeResult": 30221.8,
        "pair": "BTC"
    },
    {
        "amount": 20,
        "profit": 39,
        "status": "CLOSED",
        "type": "SELL",
        "walletType": "DEMO",
        "createdAt": "2023-07-08T11:32:06.000Z",
        "closeOrder": 30205,
        "closeResult": 30204.99,
        "pair": "BTC"
    },
    {
        "amount": 10,
        "profit": 0,
        "status": "CLOSED",
        "type": "SELL",
        "walletType": "DEMO",
        "createdAt": "2023-07-08T11:29:07.000Z",
        "closeOrder": 30196,
        "closeResult": 30196.01,
        "pair": "BTC"
    },
    {
        "amount": 10,
        "profit": 0,
        "status": "CLOSED",
        "type": "BUY",
        "walletType": "DEMO",
        "createdAt": "2023-07-08T02:37:11.000Z",
        "closeOrder": 30323.01,
        "closeResult": 30323,
        "pair": "BTC"
    },
    {
        "amount": 10,
        "profit": 0,
        "status": "CLOSED",
        "type": "SELL",
        "walletType": "DEMO",
        "createdAt": "2023-07-08T02:35:14.000Z",
        "closeOrder": 30326.7,
        "closeResult": 30329.79,
        "pair": "BTC"
    },
    {
        "amount": 10,
        "profit": 19.5,
        "status": "CLOSED",
        "type": "BUY",
        "walletType": "DEMO",
        "createdAt": "2023-07-08T02:35:07.000Z",
        "closeOrder": 30326.7,
        "closeResult": 30329.79,
        "pair": "BTC"
    },
    {
        "amount": 10,
        "profit": 0,
        "status": "CLOSED",
        "type": "BUY",
        "walletType": "DEMO",
        "createdAt": "2023-07-08T02:14:15.000Z",
        "closeOrder": 30296.93,
        "closeResult": 30286.62,
        "pair": "BTC"
    },
    {
        "amount": 10,
        "profit": 10,
        "status": "CLOSED",
        "type": "BUY",
        "walletType": "DEMO",
        "createdAt": "2023-07-08T02:05:07.000Z",
        "closeOrder": 30294.41,
        "closeResult": 30294.41,
        "pair": "BTC"
    },
    {
        "amount": 10,
        "profit": 0,
        "status": "CLOSED",
        "type": "BUY",
        "walletType": "DEMO",
        "createdAt": "2023-04-18T02:27:16.000Z",
        "closeOrder": 29431.03,
        "closeResult": 29431.02,
        "pair": "BTC"
    },
    {
        "amount": 10,
        "profit": 0,
        "status": "CLOSED",
        "type": "BUY",
        "walletType": "DEMO",
        "createdAt": "2023-04-18T02:27:11.000Z",
        "closeOrder": 29431.03,
        "closeResult": 29431.02,
        "pair": "BTC"
    },
    {
        "amount": 1,
        "profit": 1.95,
        "status": "CLOSED",
        "type": "SELL",
        "walletType": "DEMO",
        "createdAt": "2023-04-18T02:26:20.000Z",
        "closeOrder": 29433.35,
        "closeResult": 29431.13,
        "pair": "BTC"
    },
    {
        "amount": 10,
        "profit": 19.5,
        "status": "CLOSED",
        "type": "SELL",
        "walletType": "DEMO",
        "createdAt": "2023-04-18T02:25:21.000Z",
        "closeOrder": 29438.7,
        "closeResult": 29437.84,
        "pair": "BTC"
    }
]

# Convert data to a DataFrame
df = pd.DataFrame(trading_data)

# Extract price information
df['Price'] = (df['closeOrder'] + df['closeResult']) / 2

# Calculate a short-term moving average
short_window = 5
df['Short_MA'] = df['Price'].rolling(window=short_window).mean()

# Calculate a long-term moving average
long_window = 10
df['Long_MA'] = df['Price'].rolling(window=long_window).mean()

# Define a threshold for making predictions
threshold = 0.001  # Example threshold, adjust as needed

# Make predictions based on moving average crossover
df['Prediction'] = 'No Change'  # Default to no change
df.loc[df['Short_MA'] > df['Long_MA'] * (1 + threshold), 'Prediction'] = 'Up'
df.loc[df['Short_MA'] < df['Long_MA'] * (1 - threshold), 'Prediction'] = 'Down'

# Print the predictions
print(df[['Price', 'Prediction']])