import plotly.express as px, pandas as pd, matplotlib.pyplot as plt
import plotly.offline as pyo

df = px.data.medals_long()
subdf = df.query("nation=='China'")

# To create bar chart (for China in this example)
fg = px.bar(data_frame=subdf, x="medal", y="count")

# You can even create a stacked bar graph by including the 'color' argument
fg = px.bar(data_frame=df, x="medal", y="count", color="nation")

# And you can even add patterns
fg = px.bar(data_frame=df, x="medal", y="count", color="nation", pattern_shape="nation")

# Or if you want to create another type of stacked bar plot which creates bars according the 'y' axis value, then you can introduce another argument called 'base'.
fg = px.bar(data_frame=df, x="medal", y="count", base="nation", color="nation")

# To create a grouped bar chart (which is quite hard to create in matplotlib)
fg = px.bar(data_frame=df, x="medal", y="count", color="nation", barmode="group")

# Moreover, there is another type of bar graph too, though, it is important only for those who will be going to data field  
fg = px.bar_polar(data_frame=df, r="nation", theta="count", color="medal")

pyo.plot(fg)

# These are the only things that you require to create your bar graph and beautify it! In next chapter, we will see about area plots.
