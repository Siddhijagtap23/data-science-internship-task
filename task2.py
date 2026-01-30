import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_scores.csv")

plt.hist(df['Scores'])
plt.title("Distribution of Student Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df['Hours'], df['Scores'])
plt.title("Hours Studied vs Scores")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.show()
