import pandas as pd
import plotly.express as px

df=pd.read_csv("line_chart.csv")
fig=px.line(df,x="Date",y="Number of cases on that date",title="Covid",)
fig.show()