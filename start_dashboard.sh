#!/bin/bash
# CSRR Faculty Tracker Dashboard Startup Script

echo "Starting CSRR Faculty Tracker Dashboard..."

# Change to the dashboard directory
cd /Users/azrabano/csrr-dashboard

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "Virtual environment activated"
fi

# Install requirements if needed
if [ ! -f ".requirements_installed" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
    touch .requirements_installed
fi

# Start the Flask application
echo "Starting Flask application on http://localhost:5000"
python app.py

echo "Dashboard stopped."
