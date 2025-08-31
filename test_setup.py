#!/usr/bin/env python3
"""
Test script to verify that all dependencies are properly installed
and the dashboard can be imported successfully.
"""

def test_imports():
    """Test all required imports"""
    print("Testing imports...")
    
    try:
        import tkinter as tk
        print("✓ tkinter - OK")
    except ImportError as e:
        print(f"✗ tkinter - FAILED: {e}")
        return False
    
    try:
        from tkinter import ttk, messagebox, scrolledtext
        print("✓ tkinter components - OK")
    except ImportError as e:
        print(f"✗ tkinter components - FAILED: {e}")
        return False
    
    try:
        import pandas as pd
        print(f"✓ pandas {pd.__version__} - OK")
    except ImportError as e:
        print(f"✗ pandas - FAILED: {e}")
        return False
    
    try:
        import numpy as np
        print(f"✓ numpy {np.__version__} - OK")
    except ImportError as e:
        print(f"✗ numpy - FAILED: {e}")
        return False
    
    try:
        import matplotlib.pyplot as plt
        print(f"✓ matplotlib {plt.matplotlib.__version__} - OK")
    except ImportError as e:
        print(f"✗ matplotlib - FAILED: {e}")
        return False
    
    try:
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        print("✓ matplotlib backend - OK")
    except ImportError as e:
        print(f"✗ matplotlib backend - FAILED: {e}")
        return False
    
    try:
        import scipy
        from scipy import stats
        print(f"✓ scipy {scipy.__version__} - OK")
    except ImportError as e:
        print(f"✗ scipy - FAILED: {e}")
        return False
    
    try:
        from ibapi.client import EClient
        from ibapi.wrapper import EWrapper
        from ibapi.contract import Contract
        print("✓ ibapi - OK")
    except ImportError as e:
        print(f"✗ ibapi - FAILED: {e}")
        print("  Note: ibapi is only needed if you want to connect to Interactive Brokers")
        print("  You can still run the dashboard without it for testing")
    
    return True

def test_dashboard_import():
    """Test if the dashboard can be imported"""
    print("\nTesting dashboard imports...")
    
    try:
        import option_trading_dashboard
        print("✓ option_trading_dashboard.py - OK")
    except ImportError as e:
        print(f"✗ option_trading_dashboard.py - FAILED: {e}")
        return False
    
    try:
        import dashboard
        print("✓ dashboard.py - OK")
    except ImportError as e:
        print(f"✗ dashboard.py - FAILED: {e}")
        return False
    
    return True

def main():
    """Main test function"""
    print("=" * 50)
    print("Volatility Trading Dashboard - Setup Test")
    print("=" * 50)
    
    # Test imports
    imports_ok = test_imports()
    
    # Test dashboard imports
    dashboard_ok = test_dashboard_import()
    
    print("\n" + "=" * 50)
    if imports_ok and dashboard_ok:
        print("✓ ALL TESTS PASSED!")
        print("\nYou can now run the dashboard with:")
        print("  python option_trading_dashboard.py")
        print("  or")
        print("  python dashboard.py")
    else:
        print("✗ SOME TESTS FAILED!")
        print("\nPlease install missing dependencies:")
        print("  pip install -r requirements.txt")
    
    print("=" * 50)

if __name__ == "__main__":
    main() 