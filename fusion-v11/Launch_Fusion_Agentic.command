#!/bin/bash

# Fusion v12.2 Universal Launcher
cd "$(dirname "$0")"

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3 and try again."
    exit 1
fi

# Create and activate virtual environment if needed
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Display menu
echo "Fusion v12.2 - Universal Launcher"
echo "--------------------------------"
echo "1. Simulate Mode (Component + Design Tech Focus)"
echo "2. Ship Mode (SLT-Quality Production)"
echo "3. Critique Mode (Analysis + Improvement)"
echo "4. Prototype Mode (Rapid Implementation)"
echo "5. Pattern Development"
echo "6. Debug Mode"
echo "7. Exit"
echo

read -p "Select mode (1-7): " mode

case $mode in
    1)
        python fusion_cli.py simulate
        ;;
    2)
        python fusion_cli.py ship
        ;;
    3)
        python fusion_cli.py critique
        ;;
    4)
        python fusion_cli.py prototype
        ;;
    5)
        python pattern_dev.py -l
        read -p "Enter pattern name to test: " pattern
        python pattern_dev.py $pattern
        ;;
    6)
        python fusion.py --debug
        ;;
    7)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid selection"
        exit 1
        ;;
esac 