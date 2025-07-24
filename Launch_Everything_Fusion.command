#!/bin/bash

# 🚀 FUSION V11 COMPLETE LAUNCH SCRIPT
# Installs, configures, and launches the entire Fusion v11 system
# Compatible with macOS, designed for Cursor integration

echo "🚀 FUSION V11 COMPLETE LAUNCH SYSTEM"
echo "======================================"
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

echo "📍 Working Directory: $SCRIPT_DIR"
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install Python packages
install_python_packages() {
    echo "📦 Installing Python dependencies..."
    
    # Try pip3 first, then pip
    if command_exists pip3; then
        PIP_CMD="pip3"
    elif command_exists pip; then
        PIP_CMD="pip"
    else
        echo "❌ ERROR: pip not found. Please install Python first."
        exit 1
    fi
    
    # Install required packages
    echo "Installing numpy (may take a moment)..."
    $PIP_CMD install numpy --quiet
    
    echo "Installing additional dependencies..."
    $PIP_CMD install --quiet \
        requests \
        datetime \
        typing \
        enum34 \
        json5
    
    echo "✅ Python dependencies installed successfully"
    echo ""
}

# Function to check Python installation
check_python() {
    echo "🐍 Checking Python installation..."
    
    if command_exists python3; then
        PYTHON_CMD="python3"
        PYTHON_VERSION=$(python3 --version 2>&1)
        echo "✅ Found: $PYTHON_VERSION"
    elif command_exists python; then
        PYTHON_CMD="python"
        PYTHON_VERSION=$(python --version 2>&1)
        echo "✅ Found: $PYTHON_VERSION"
    else
        echo "❌ ERROR: Python not found. Please install Python 3.7+ first."
        echo "Visit: https://www.python.org/downloads/"
        exit 1
    fi
    echo ""
}

# Function to test Fusion v11 installation
test_fusion_installation() {
    echo "🧪 Testing Fusion v11 installation..."
    
    # Test the simple version first (most likely to work)
    if [ -f "fusion_v11_context_simple.py" ]; then
        echo "Testing fusion_v11_context_simple.py..."
        $PYTHON_CMD fusion_v11_context_simple.py > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo "✅ Simple version working perfectly"
            WORKING_VERSION="fusion_v11_context_simple.py"
        else
            echo "⚠️  Simple version has issues, trying enhanced version..."
        fi
    fi
    
    # Test the enhanced version
    if [ -f "fusion_v11_enhanced_with_cofounder_learnings.py" ]; then
        echo "Testing fusion_v11_enhanced_with_cofounder_learnings.py..."
        $PYTHON_CMD fusion_v11_enhanced_with_cofounder_learnings.py > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo "✅ Enhanced version working perfectly"
            WORKING_VERSION="fusion_v11_enhanced_with_cofounder_learnings.py"
        else
            echo "⚠️  Enhanced version has dependency issues"
        fi
    fi
    
    echo ""
}

# Function to create interactive launcher
create_interactive_launcher() {
    echo "🎯 Creating interactive launcher..."
    
    cat > fusion_interactive_launcher.py << 'EOF'
#!/usr/bin/env python3
"""
Fusion v11 Interactive Launcher
Provides an interactive interface to launch and use Fusion v11 system
"""

import os
import sys
import subprocess
import json
from datetime import datetime

class FusionInteractiveLauncher:
    def __init__(self):
        self.working_versions = []
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.detect_working_versions()
    
    def detect_working_versions(self):
        """Detect which Fusion v11 versions are working."""
        versions_to_test = [
            ("Simple Context Engineering", "fusion_v11_context_simple.py"),
            ("Enhanced with Cofounder Learnings", "fusion_v11_enhanced_with_cofounder_learnings.py"),
            ("Advanced Context Engineering", "fusion_v11_context_engineering_advanced.py")
        ]
        
        for name, filename in versions_to_test:
            if os.path.exists(os.path.join(self.current_dir, filename)):
                self.working_versions.append((name, filename))
    
    def show_main_menu(self):
        """Display the main menu."""
        print("\n🚀 FUSION V11 INTERACTIVE LAUNCHER")
        print("=" * 50)
        print(f"📍 Location: {self.current_dir}")
        print(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n📋 AVAILABLE OPTIONS:")
        print("")
        
        print("1. 🎯 Quick Demo - Run with crypto trading challenge")
        print("2. 🔧 Custom Challenge - Enter your own design challenge") 
        print("3. 📊 System Information - View available versions")
        print("4. 📖 Documentation - View integration guides")
        print("5. 🎮 Interactive Mode - Step-by-step guided experience")
        print("6. 🌐 Cursor Integration - Setup for Cursor IDE")
        print("7. ❌ Exit")
        print("")
    
    def run_quick_demo(self):
        """Run the quick demo with crypto trading challenge."""
        print("\n🎯 RUNNING QUICK DEMO")
        print("=" * 30)
        
        if not self.working_versions:
            print("❌ No working versions found. Please check installation.")
            return
        
        # Use the first working version
        version_name, version_file = self.working_versions[0]
        print(f"Using: {version_name}")
        print(f"File: {version_file}")
        print("")
        
        try:
            result = subprocess.run([sys.executable, version_file], 
                                  capture_output=True, text=True, cwd=self.current_dir)
            
            if result.returncode == 0:
                print("✅ Demo completed successfully!")
                print("\n📊 OUTPUT:")
                print(result.stdout)
            else:
                print("❌ Demo failed with errors:")
                print(result.stderr)
                
        except Exception as e:
            print(f"❌ Error running demo: {e}")
    
    def run_custom_challenge(self):
        """Run with custom design challenge."""
        print("\n🔧 CUSTOM DESIGN CHALLENGE")
        print("=" * 30)
        
        challenge = input("Enter your design challenge: ").strip()
        if not challenge:
            print("❌ No challenge entered.")
            return
        
        print(f"\n🎯 Processing challenge: {challenge}")
        print("⚠️  Note: Custom challenge integration requires code modification.")
        print("📖 See documentation for programmatic usage examples.")
    
    def show_system_info(self):
        """Show system information."""
        print("\n📊 SYSTEM INFORMATION")
        print("=" * 30)
        
        print(f"📂 Working Directory: {self.current_dir}")
        print(f"🐍 Python: {sys.executable}")
        print(f"📋 Python Version: {sys.version}")
        print("")
        
        print("🔧 AVAILABLE FUSION V11 VERSIONS:")
        if self.working_versions:
            for i, (name, filename) in enumerate(self.working_versions, 1):
                print(f"  {i}. {name} ({filename})")
        else:
            print("  ❌ No working versions detected")
        print("")
        
        print("📁 AVAILABLE FILES:")
        fusion_files = [f for f in os.listdir(self.current_dir) 
                       if f.startswith('fusion_') and f.endswith('.py')]
        for file in sorted(fusion_files):
            print(f"  • {file}")
    
    def show_documentation(self):
        """Show documentation links."""
        print("\n📖 DOCUMENTATION")
        print("=" * 20)
        
        docs = [
            ("Complete Ship-Today Package", "FUSION_V11_SHIP_TODAY_PACKAGE.md"),
            ("Cofounder v11 Analysis", "COFOUNDER_V11_ORCHESTRATION_ANALYSIS.md"),
            ("Context Engineering Integration", "CONTEXT_ENGINEERING_INTEGRATION_SUMMARY.md")
        ]
        
        for name, filename in docs:
            if os.path.exists(os.path.join(self.current_dir, filename)):
                print(f"✅ {name}: {filename}")
            else:
                print(f"❌ {name}: {filename} (not found)")
    
    def show_cursor_integration(self):
        """Show Cursor integration instructions."""
        print("\n🌐 CURSOR INTEGRATION SETUP")
        print("=" * 30)
        
        print("📋 TO USE WITH CURSOR IDE:")
        print("")
        print("1. 🎯 IMPORT AS PROJECT:")
        print(f"   - Open Cursor IDE")
        print(f"   - File → Open Folder")
        print(f"   - Select: {self.current_dir}")
        print("")
        
        print("2. 🔧 CONFIGURE PYTHON:")
        print("   - Cmd+Shift+P (macOS) or Ctrl+Shift+P (Windows)")
        print("   - Type: 'Python: Select Interpreter'")
        print(f"   - Select: {sys.executable}")
        print("")
        
        print("3. 🚀 RUN FUSION V11:")
        print("   - Open terminal in Cursor (Ctrl+`)")
        print("   - Run: python3 fusion_v11_context_simple.py")
        print("   - Or use Cursor's run button on any .py file")
        print("")
        
        print("4. 🎨 USAGE IN CURSOR:")
        print("   - Modify fusion files directly in Cursor")
        print("   - Use Cursor's AI chat with Fusion v11 context")
        print("   - Integrate with Cursor's code generation")
        print("")
        
        print("5. 📝 RECOMMENDED WORKFLOW:")
        print("   - Chat with Cursor AI about design challenges")
        print("   - Run Fusion v11 for detailed analysis")
        print("   - Use results to guide Cursor code generation")
        print("   - Iterate with Fusion v11 feedback")
    
    def interactive_mode(self):
        """Run interactive guided experience."""
        print("\n🎮 INTERACTIVE GUIDED EXPERIENCE")
        print("=" * 35)
        
        print("🎯 This mode guides you through using Fusion v11 step by step.")
        print("")
        
        # Step 1: Choose version
        print("📋 STEP 1: Choose Fusion v11 Version")
        if len(self.working_versions) > 1:
            for i, (name, filename) in enumerate(self.working_versions, 1):
                print(f"  {i}. {name}")
            
            choice = input("Enter choice (1-{}): ".format(len(self.working_versions))).strip()
            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(self.working_versions):
                    selected_version = self.working_versions[choice_idx]
                    print(f"✅ Selected: {selected_version[0]}")
                else:
                    print("❌ Invalid choice, using first available version")
                    selected_version = self.working_versions[0]
            except ValueError:
                print("❌ Invalid input, using first available version")
                selected_version = self.working_versions[0]
        else:
            selected_version = self.working_versions[0] if self.working_versions else None
            
        if not selected_version:
            print("❌ No working versions available")
            return
        
        # Step 2: Choose challenge type
        print("\n📋 STEP 2: Choose Challenge Type")
        print("  1. Crypto trading authentication (demo)")
        print("  2. E-commerce checkout flow")
        print("  3. Mobile app onboarding")
        print("  4. Custom challenge")
        
        challenge_choice = input("Enter choice (1-4): ").strip()
        
        challenges = {
            "1": "Design a cryptocurrency trading authentication system that builds trust for newcomers while providing advanced security features for experienced traders.",
            "2": "Design an e-commerce checkout flow that minimizes cart abandonment while maintaining security and trust.",
            "3": "Design a mobile app onboarding experience that educates users without overwhelming them.",
            "4": None
        }
        
        if challenge_choice == "4":
            custom_challenge = input("Enter your custom challenge: ").strip()
            selected_challenge = custom_challenge if custom_challenge else challenges["1"]
        else:
            selected_challenge = challenges.get(challenge_choice, challenges["1"])
        
        print(f"\n✅ Selected challenge: {selected_challenge[:60]}...")
        
        # Step 3: Run analysis
        print("\n📋 STEP 3: Running Fusion v11 Analysis")
        print("🔄 Processing... (this may take a moment)")
        
        try:
            result = subprocess.run([sys.executable, selected_version[1]], 
                                  capture_output=True, text=True, cwd=self.current_dir)
            
            if result.returncode == 0:
                print("✅ Analysis completed successfully!")
                print("\n📊 KEY INSIGHTS:")
                # Extract key lines from output
                output_lines = result.stdout.split('\n')
                for line in output_lines[:10]:  # Show first 10 lines
                    if line.strip():
                        print(f"  • {line.strip()}")
                
                print(f"\n📖 Full output available in terminal above")
            else:
                print("❌ Analysis failed:")
                print(result.stderr)
                
        except Exception as e:
            print(f"❌ Error running analysis: {e}")
        
        print("\n🎯 NEXT STEPS:")
        print("  • Review the full output above")
        print("  • Modify fusion files for your specific needs")
        print("  • Integrate insights into your design process")
        print("  • Use with Cursor IDE for enhanced workflow")
    
    def run(self):
        """Run the interactive launcher."""
        while True:
            self.show_main_menu()
            
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == "1":
                self.run_quick_demo()
            elif choice == "2":
                self.run_custom_challenge()
            elif choice == "3":
                self.show_system_info()
            elif choice == "4":
                self.show_documentation()
            elif choice == "5":
                self.interactive_mode()
            elif choice == "6":
                self.show_cursor_integration()
            elif choice == "7":
                print("\n👋 Goodbye! Happy designing with Fusion v11!")
                break
            else:
                print("❌ Invalid choice. Please try again.")
            
            input("\n⏸️  Press Enter to continue...")

if __name__ == "__main__":
    launcher = FusionInteractiveLauncher()
    launcher.run()
EOF

    echo "✅ Interactive launcher created: fusion_interactive_launcher.py"
    echo ""
}

# Function to create quick test script
create_quick_test() {
    echo "🧪 Creating quick test script..."
    
    cat > test_fusion_quick.py << 'EOF'
#!/usr/bin/env python3
"""
Quick Fusion v11 Test Script
Tests all available versions and shows which ones work
"""

import os
import sys
import subprocess
import time

def test_fusion_version(filename):
    """Test a specific Fusion v11 version."""
    if not os.path.exists(filename):
        return False, f"File not found: {filename}"
    
    try:
        start_time = time.time()
        result = subprocess.run([sys.executable, filename], 
                              capture_output=True, text=True, timeout=30)
        end_time = time.time()
        
        if result.returncode == 0:
            return True, f"Success in {end_time - start_time:.2f}s"
        else:
            return False, f"Error: {result.stderr[:100]}..."
            
    except subprocess.TimeoutExpired:
        return False, "Timeout (>30s)"
    except Exception as e:
        return False, f"Exception: {str(e)}"

def main():
    print("🧪 FUSION V11 QUICK TEST")
    print("=" * 30)
    
    versions_to_test = [
        ("Simple Context", "fusion_v11_context_simple.py"),
        ("Enhanced Cofounder", "fusion_v11_enhanced_with_cofounder_learnings.py"),
        ("Advanced Context", "fusion_v11_context_engineering_advanced.py")
    ]
    
    working_versions = []
    
    for name, filename in versions_to_test:
        print(f"Testing {name}...")
        success, message = test_fusion_version(filename)
        
        if success:
            print(f"✅ {name}: {message}")
            working_versions.append((name, filename))
        else:
            print(f"❌ {name}: {message}")
    
    print(f"\n📊 SUMMARY")
    print(f"Working versions: {len(working_versions)}/{len(versions_to_test)}")
    
    if working_versions:
        print(f"\n🚀 RECOMMENDED VERSION:")
        best_version = working_versions[0]
        print(f"   {best_version[0]} ({best_version[1]})")
        print(f"\n💡 TO RUN: python3 {best_version[1]}")
    else:
        print("\n❌ No working versions found. Check dependencies.")

if __name__ == "__main__":
    main()
EOF

    echo "✅ Quick test script created: test_fusion_quick.py"
    echo ""
}

# Function to show final instructions
show_final_instructions() {
    echo "🎉 FUSION V11 INSTALLATION COMPLETE!"
    echo "====================================="
    echo ""
    echo "🚀 HOW TO USE:"
    echo ""
    echo "1. 🎯 INTERACTIVE LAUNCHER (Recommended):"
    echo "   $PYTHON_CMD fusion_interactive_launcher.py"
    echo ""
    echo "2. 🧪 QUICK TEST:"
    echo "   $PYTHON_CMD test_fusion_quick.py"
    echo ""
    echo "3. 🎮 DIRECT USAGE:"
    if [ -n "$WORKING_VERSION" ]; then
        echo "   $PYTHON_CMD $WORKING_VERSION"
    else
        echo "   $PYTHON_CMD fusion_v11_context_simple.py"
    fi
    echo ""
    echo "4. 🌐 CURSOR INTEGRATION:"
    echo "   - Open this folder in Cursor IDE"
    echo "   - Configure Python interpreter: $PYTHON_CMD"
    echo "   - Run any .py file using Cursor's run button"
    echo "   - Use interactive launcher for guided experience"
    echo ""
    echo "📍 LOCATION: $SCRIPT_DIR"
    echo "📖 DOCUMENTATION: See .md files in this folder"
    echo ""
    echo "🎯 READY TO USE FUSION V11!"
}

# Main execution flow
main() {
    echo "Starting Fusion v11 installation and setup..."
    echo ""
    
    # Step 1: Check Python
    check_python
    
    # Step 2: Install dependencies
    install_python_packages
    
    # Step 3: Test installation
    test_fusion_installation
    
    # Step 4: Create interactive tools
    create_interactive_launcher
    create_quick_test
    
    # Step 5: Show final instructions
    show_final_instructions
    
    # Step 6: Ask if user wants to launch now
    echo "🚀 LAUNCH NOW?"
    echo "1. Yes - Launch interactive launcher"
    echo "2. Yes - Run quick test"
    echo "3. No - I'll launch manually later"
    echo ""
    
    read -p "Enter choice (1-3): " launch_choice
    
    case $launch_choice in
        1)
            echo ""
            echo "🚀 Launching interactive launcher..."
            $PYTHON_CMD fusion_interactive_launcher.py
            ;;
        2)
            echo ""
            echo "🧪 Running quick test..."
            $PYTHON_CMD test_fusion_quick.py
            ;;
        3)
            echo ""
            echo "👋 Setup complete! Launch when ready."
            ;;
        *)
            echo ""
            echo "👋 Setup complete! Use the instructions above to launch."
            ;;
    esac
}

# Run main function
main

echo ""
echo "🎯 Fusion v11 setup script completed!"
echo "📍 You can always re-run this script to reinstall or get instructions." 