import plotly.express as px, pandas as pd, matplotlib.pyplot as plt
import plotly.offline as pyo

df = px.data.medals_long()

# To create a basic heatmap, you need to define 3 variables.
fig = px.density_heatmap(data_frame=df, x="medal", y="nation", z="count")

px.imshow(fig)