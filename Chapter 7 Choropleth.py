import plotly.express as px, pandas as pd, matplotlib.pyplot as plt
import plotly.offline as pyo

df = px.data.medals_long()
subdf = df.query("medal=='gold'")

# Choropleth is actually a world map based graph and it's used to represent a distribution which is based on different countries.

# To create a simple choropleth, you need a column which has the names of countries and then set the 'locationmode' to 'country names' which will make it accept country names from the column.
fig = px.choropleth(data_frame=subdf, locations="nation", locationmode="country names")

# You can also use it as a heatmap by using the color argument
fig = px.choropleth(data_frame=subdf, locations="nation", locationmode="country names", color="count")

# You can also set a scope which tells 'px' to focus on a particular continent. By default, it's world.
fig = px.choropleth(data_frame=subdf, locations="nation", locationmode="country names", color="count")

# You can define map size by using 'projection'
fig = px.choropleth(data_frame=subdf, locations="nation", locationmode="country names", color="count", projection="mercator")
fig = px.choropleth(data_frame=subdf, locations="nation", locationmode="country names", color="count", projection="hammer")
fig = px.choropleth(data_frame=subdf, locations="nation", locationmode="country names", color="count", projection="robinson")
fig = px.choropleth(data_frame=subdf, locations="nation", locationmode="country names", color="count", projection="natural earth")
fig = px.choropleth(data_frame=subdf, locations="nation", locationmode="country names", color="count", projection="orthographic")



pyo.plot(fig)