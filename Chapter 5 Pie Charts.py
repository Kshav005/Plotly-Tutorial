import plotly.express as px, pandas as pd, matplotlib.pyplot as plt
import plotly.offline as pyo

df = px.data.medals_long()
subdf = df.query("medal=='gold'")

# To create a pie chart, you need to pass in 2 values - names (it will be set as colors for labels) and values (for calculation of values)
fig = px.pie(data_frame=subdf, names="nation", values="count")

# To convert your pie chart to a donut chart, use 'hole' between 0 to 1
fig = px.pie(subdf, names="nation", values="count", hole=0.6)

pyo.plot(fig)

# Pie charts are pretty short but important and hence it doesn't need a lot of arguments.