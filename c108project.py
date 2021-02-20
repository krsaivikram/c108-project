import pandas as pd 
import plotly.figure_factory as ff
import csv
file = pd.read_csv("C:/Users/Manorama/Desktop/mobile.csv")
fig = ff.create_distplot([file["Avg Rating"].tolist()],["average rating"])
fig.show()