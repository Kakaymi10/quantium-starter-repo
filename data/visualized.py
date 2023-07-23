import pandas as pd
from dash import Dash, dcc, html
import plotly.graph_objs as go

# Read the data from the output CSV file
data = pd.read_csv('output.csv')

# Check if 'date' column exists in the DataFrame
if 'date' in data.columns:
    # Convert the 'date' column to a datetime object for proper sorting
    data['date'] = pd.to_datetime(data['date'])
    # Sort the data by date
    data = data.sort_values(by='date')

# Create a Dash app
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Sales Data Visualizer'),
    
    dcc.Graph(
        id='line-chart',
        figure={
            'data': [
                go.Scatter(
                    x=data['date'],
                    y=data['sales'].replace({'\$': ''}, regex=True).astype(float),
                    mode='lines',
                    marker={'color': 'blue'},
                    name='Sales'
                )
            ],
            'layout': go.Layout(
                title='Daily Sales Data',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Sales'},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
