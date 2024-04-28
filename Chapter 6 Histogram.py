import plotly.express as px, pandas as pd, matplotlib.pyplot as plt
import plotly.offline as pyo

df = [34, 54, 64, 34, 23, 32, 43, 342, 234, 23, 323, 53, 43]

# To create histogram
fig = px.histogram(x=df)

# You can define an extra plot using 'marginal' which can have - violin, box, rug or histogram
fig = px.histogram(x=df, marginal="rug")

# You can set it for cumulative values
fig = px.histogram(x=df, cumulative=True)

pyo.plot(fig)