#!/bin/bash

# Volatility Trading Dashboard Launcher
# This script activates the virtual environment and runs the dashboard

echo "Starting Volatility Trading Dashboard..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Error: Virtual environment not found. Please run setup first."
    echo "Run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check which dashboard to run
if [ "$1" = "alt" ]; then
    echo "Running alternative dashboard (dashboard.py)..."
    python dashboard.py
else
    echo "Running main dashboard (option_trading_dashboard.py)..."
    python option_trading_dashboard.py
fi 