import pandas as pd
from dash import Dash, dcc, html, Input, Output
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
    html.H1(children='Sales Data Visualizer', style={'textAlign': 'center', 'color': 'blue'}),
    
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',
        style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'center', 'marginBottom': '20px'}
    ),
    
    dcc.Graph(
        id='line-chart',
        config={'displayModeBar': False},
        figure={}
    )
])

# Define callback to update the line chart based on the selected region
@app.callback(
    Output('line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_line_chart(selected_region):
    if selected_region == 'all':
        filtered_data = data
    else:
        filtered_data = data[data['region'] == selected_region]
    
    trace = go.Scatter(
        x=filtered_data['date'],
        y=filtered_data['sales'].replace({'\$': ''}, regex=True).astype(float),
        mode='lines',
        marker={'color': 'blue'},
        name='Sales'
    )
    
    layout = go.Layout(
        title='Daily Sales Data',
        xaxis={'title': 'Date'},
        yaxis={'title': 'Sales'},
        hovermode='closest'
    )
    
    return {'data': [trace], 'layout': layout}

if __name__ == '__main__':
    app.run_server(debug=True)
