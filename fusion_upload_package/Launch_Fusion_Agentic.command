#!/bin/bash
# Fusion v11.2 Agentic Pattern System Launcher

cd "$(dirname "$0")"

# Check Python
if ! command -v python3 &> /dev/null; then
  echo "Python3 not found. Please install Python 3.7 or higher."
  exit 1
fi

# Install dependencies
if [ -f requirements.txt ]; then
  echo "Installing Python dependencies..."
  python3 -m pip install --upgrade pip
  python3 -m pip install -r requirements.txt
fi

# Verify pattern system
echo "Running pattern system test..."
python3 test_stepwise_insight_synthesis.py
python3 test_role_directive.py
python3 test_pattern_critique_then_rewrite.py

# Launch main agentic workflow (customize as needed)
echo "Fusion v11.2 Agentic Pattern System is ready!"
echo "You can now run your main agent workflows or import modules in Cursor/ChatGPT." 