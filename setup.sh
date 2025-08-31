#!/bin/bash

# Volatility Trading Dashboard Setup Script
# This script sets up the virtual environment and installs all dependencies

echo "Setting up Volatility Trading Dashboard..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is not installed. Please install pip3 first."
    exit 1
fi

# Install system dependencies
echo "Installing system dependencies..."
sudo apt update
sudo apt install -y python3-tk python3-venv

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment and install Python packages
echo "Installing Python packages..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Make launcher script executable
chmod +x run_dashboard.sh

echo ""
echo "Setup complete! You can now run the dashboard with:"
echo "  ./run_dashboard.sh"
echo ""
echo "Or manually with:"
echo "  source venv/bin/activate"
echo "  python option_trading_dashboard.py"
echo ""
echo "Note: You'll need Interactive Brokers TWS or IB Gateway running"
echo "to connect to market data." 