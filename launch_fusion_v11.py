#!/usr/bin/env python3
"""
Fusion V11 Production System Launcher
=====================================

Simple launcher script to run the complete Fusion V11 system.
"""

import asyncio
import sys
import os

def main():
    """Main launcher function"""
    print("🚀 Fusion V11 Production System Launcher")
    print("=" * 50)
    
    # Check if the main system file exists
    if not os.path.exists("fusion_v11_production_complete.py"):
        print("❌ Error: fusion_v11_production_complete.py not found!")
        print("Please ensure you're in the correct directory.")
        return 1
    
    # Import and run the system
    try:
        from fusion_v11_production_complete import run_comprehensive_demo
        
        print("🎯 Running Fusion V11 comprehensive demonstration...")
        print("This will showcase the complete context engineering system.\n")
        
        # Run the demo
        asyncio.run(run_comprehensive_demo())
        
        print("\n✅ Demo completed successfully!")
        print("📝 Check the exported JSON file for detailed results.")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please ensure all dependencies are installed:")
        print("pip install -r requirements_production.txt")
        return 1
    except Exception as e:
        print(f"❌ Error running demo: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 