import pandas as pd

df = pd.read_csv("student_scores.csv")

print("First 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())