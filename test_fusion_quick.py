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
