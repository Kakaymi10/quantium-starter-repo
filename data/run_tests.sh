#!/bin/bash

# Activate the project virtual environment
source venv/bin/activate

# Execute the test suite using Pytest
pytest test_app.py

# Capture the exit code of the last command
EXIT_CODE=$?

# Deactivate the virtual environment
deactivate

# Return the exit code
exit $EXIT_CODE
