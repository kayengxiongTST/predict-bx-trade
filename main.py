import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate sample data (replace with your real data)
np.random.seed(42)
num_days = 100
prices = np.cumsum(np.random.randn(num_days)) + 100
print(prices)

# Create a DataFrame with date and price columns
dates = pd.date_range(start='2023-01-01', periods=num_days)
data = {'Date': dates, 'Price': prices}
df = pd.DataFrame(data)

# Feature engineering: Calculate moving averages
window_size = 10
df['MA'] = df['Price'].rolling(window=window_size).mean()

# Drop rows with NaN values
df.dropna(inplace=True)

# Split the data into training and testing sets
X = df[['MA']].values
y = df['Price'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict using the trained model
y_pred = model.predict(X_test)

# Plot the actual and predicted prices
plt.figure(figsize=(10, 6))
plt.scatter(df['Date'].iloc[-len(y_test):], y_test, label='Actual Prices')
plt.plot(df['Date'].iloc[-len(y_test):], y_pred, color='red', label='Predicted Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price Prediction')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
