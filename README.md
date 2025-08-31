# Volatility Trading Dashboard

A Python application built for analyzing implied voltilty using Interactive Brokers API to provide real-time market data analysis through an interactive dashboard.

## What It Does

The dashboard connects to IB TWS/Gateway to fetch live options data, calculates implied volatility percentiles and regimes, and generates statistical analysis including forward volatility predictions and mean reversion signals. It features a three-panel visualization system that updates in real-time as market data streams in.

## Technologies Used

- **Python 3.7+** with pandas for data manipulation and statistical analysis
- **Interactive Brokers API** (ibapi) for real-time market data connectivity
- **Matplotlib & Seaborn** for statistical visualization and plotting
- **Tkinter** for the interactive GUI dashboard
- **Statistical libraries** for volatility regime detection and regression analysis

## Key Features

- Real-time implied volatility analysis with percentile calculations
- Volatility regime identification (High/Normal/Low) with color-coded indicators
- Forward volatility prediction using linear regression models
- Mean reversion trading signals based on statistical analysis
- Interactive three-panel dashboard with live updates

## Prerequisites

- Interactive Brokers account with TWS or IB Gateway
- Python 3.7+ and pip
- Market data subscriptions for options

## Quick Start

1. **Install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Start TWS/IB Gateway** and enable API connections (port 7497 for TWS, 4001 for Gateway)

3. **Run the dashboard:**
   ```bash
   ./run_dashboard.sh
   # or manually:
   source venv/bin/activate
   python option_trading_dashboard.py
   ```

4. **Connect and analyze:**
   - Enter connection details (host: 127.0.0.1, port: 7497)
   - Query IV data for any symbol (default: SPY)
   - Click "Analyze Implied Vol" to see results

## Working

This project showcases utility of financial APIs in implementing real-time data processing pipelines, and creating interactive data visualization tools. The dashboard successfully processes live market data streams while performing complex statistical computations for volatility analysis. The project includes regime detection algorithms, statistical models for forward volatility prediction, and the real-time visualization system that updates dynamically as new data arrives.

## File Structure

```
├── option_trading_dashboard.py  # Main dashboard application
├── dashboard.py                 # Alternative implementation
├── requirements.txt            # Dependencies
└── run_dashboard.sh           # Launcher script
```

