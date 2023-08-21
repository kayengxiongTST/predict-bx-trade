import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample data (replace this with your actual data)
data = [
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

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert "type" column to numerical values (SELL=0, BUY=1)
df['type'] = df['type'].apply(lambda x: 0 if x == 'SELL' else 1)

# Feature columns (you can modify or add more features)
features = ['amount', 'profit']

# Split the data into features and target
X = df[features]
y = df['type']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the classifier
clf = RandomForestClassifier(random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
predictions = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy:.2f}')

# Predict the next trade based on the last data point
last_data_point = df.iloc[-1][features].values.reshape(1, -1)
predicted_next_trade = clf.predict(last_data_point)

if predicted_next_trade == 0:
    print('Predicted next trade: SELL')
else:
    print('Predicted next trade: BUY')