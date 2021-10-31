import pandas as pd
import plotly_express as pe

df = pd.read_csv('data.csv')
scatter = pe.scatter(df, x='date', y='cases', color='country')
scatter.show()