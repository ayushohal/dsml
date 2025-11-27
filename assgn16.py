import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

plt.hist(df['fare'], bins=30)
plt.title("Distribution of Ticket Fare")
plt.xlabel("fare")
plt.ylabel("Number of Passengers")
plt.show()