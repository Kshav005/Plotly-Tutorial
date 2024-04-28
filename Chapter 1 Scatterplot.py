# In this chapter, we are going to learn about another data science module called 'plotly'
# You need to run 'pip install plotly' in your terminal in order have it installed.
# Now let's start!

# Importing it
import plotly.express as px, pandas as pd, matplotlib.pyplot as plt
import plotly.offline as pyo

# We will be using the inbuilt dataset of plotly.
df = px.data.medals_long()

fig = px.scatter(data_frame=df, x="medal", y="count")

# You don't need to use 'plt.show' for getting the graph, instead you need to create a variable and use 'pyo.plot()' on it.
# pyo.plot(fig)
# It may seem a little complicated but as you practice, you will become habitual of it.

# Let's learn about some of the arguments that can be helpful
# Color/Size/Symbol : They all work the same, basically for categorical data
fig = px.scatter(data_frame=df, x="medal", y="count", color="nation")

# You can even put a text on the scatter dots
fig = px.scatter(data_frame=df, x="medal", y="count", text="nation")

# Or opacity (from 0 to 1)
fig = px.scatter(data_frame=df, x="medal", y="count", opacity=0.4)

# Or set the title
fig = px.scatter(data_frame=df, x="medal", y="count", title="THIS IS MY GRAPH!")

pyo.plot(fig)


# We will meet in the next chapter to learn more about this library!