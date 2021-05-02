import csv
import statistics
import pandas as pd
import plotly.figure_factory as px

df = pd.read_csv("StudentsPerformance.csv")

data = []
data = df["gender"].tolist()
data = df["race/ethnicity"].tolist()
data = df["parental level of education"].tolist()
data = df["lunch"].tolist()
data = df["test preparation course"].tolist()
data = df["math score"].tolist()
data = df["reading score"].tolist()
data = df["writing score"].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
std = statistics.stdev(data)

fig = px.create_distplot([data], ["results"], show_hist = False)
fig.show()

print("The Mean of all the data is: "+mean)
print("The Median of all the data is: "+median)
print("The Mode of all the data is: "+mode)
print("The Standard Deviantion of all the data is: "+std)