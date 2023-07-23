import pytest
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app  # Assuming your Dash app is defined in a file named 'app.py'

# Define the test functions

def test_header_present():
    # Create a Dash test client
    client = app.test_client()

    # Get the app's layout
    response = client.get('/')
    layout = response.get_data(as_text=True)

    # Verify that the header is present
    assert 'Sales Data Visualizer' in layout

def test_visualization_present():
    # Create a Dash test client
    client = app.test_client()

    # Get the app's layout
    response = client.get('/')
    layout = response.get_data(as_text=True)

    # Verify that the visualization is present
    assert 'line-chart' in layout

def test_region_picker_present():
    # Create a Dash test client
    client = app.test_client()

    # Get the app's layout
    response = client.get('/')
    layout = response.get_data(as_text=True)

    # Verify that the region picker is present
    assert 'region-filter' in layout

# Execute the test suite using Pytest

if __name__ == '__main__':
    pytest.main()
