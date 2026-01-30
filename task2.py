import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_scores.csv")

# Histogram - Math marks
plt.hist(df['Math'])
plt.title("Distribution of Math Marks")
plt.xlabel("Math Marks")
plt.ylabel("Frequency")
plt.show()

# Scatter plot - Math vs Science
plt.scatter(df['Math'], df['Science'])
plt.title("Math vs Science Marks")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.show()
