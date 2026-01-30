import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load data
df = pd.read_csv("student_scores.csv")

# Input & Output
X = df[['Math']]      # independent variable
y = df['Science']    # dependent variable

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Result
print("Mean Squared Error:", mean_squared_error(y_test, predictions))
print("Model trained successfully!")