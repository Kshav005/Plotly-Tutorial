import plotly.express as px, pandas as pd, matplotlib.pyplot as plt
import plotly.offline as pyo

df = [34, 54, 64, 34, 23, 32, 43, 342, 234, 23, 323, 53, 43]
cf = px.data.medals_long()
nf = cf.query("medal=='gold'")

# For box plot
fig = px.box(x=df)

# Similiarly for violin plot
fig = px.violin(x=df)

# Strip plot is really similiar to scatter plot but it is used for counting frequencies.
fig = px.strip(x=df)

# Funnel plot
fig = px.funnel(cf, x="nation", y="count", color="medal")

# Line geo
fig = px.line_geo(nf, locationmode="country names", locations="nation", color="count")

pyo.plot(fig)