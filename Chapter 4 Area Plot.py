import plotly.express as px, pandas as pd, matplotlib.pyplot as plt
import plotly.offline as pyo

df = px.data.medals_long()


# For a simple area chart
fg = px.area(data_frame=df, x="medal", y="count", color="nation")

# Let's have a look at some more arguments which we can use.
# You can define line shapes, suppose for a curved line set 'line_shape' to 'spline'
fg = px.area(data_frame=df, x="medal", y="count", color="nation", line_shape="spline")  

# You can have patterns/symbols/texts
fg = px.area(data_frame=df, x="medal", y="count", color="nation", symbol="nation")

pyo.plot(fg)

# These are the arguments which you might need to enhance your area charts