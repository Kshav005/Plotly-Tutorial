import plotly.express as px, pandas as pd, matplotlib.pyplot as plt
import plotly.offline as pyo

df = px.data.medals_long()
sdf = df.query("medal=='gold'")

# Now we will learn about line graphs
# It is very similar to scatter plot as the main idea is connecting the dots of scatter plot to become line plot.
fig = px.line(data_frame=sdf, x="nation", y="count")

# And same arguments can be used to enhance the features
fig = px.line(data_frame=df, x="medal", y="count", color="nation")
fig = px.line(data_frame=df, x="nation", y="count", text="count")

# To disable/enable markers
fig = px.line(data_frame=df, x="nation", y="count", markers=True)

# Or categorize by different line styles
fig = px.line(data_frame=df, x="nation", y="count", line_dash="medal")

pyo.plot(fig)

# That's all you can learn about the line graph and that's enough! If you need to advance through it, then read the documentation for a lot more information.
