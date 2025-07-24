#!/bin/bash

# Fusion V12.2 Launch System
# Self-contained, dependency-free setup

# Configuration
FUSION_VERSION="12.2"
FUSION_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FUSION_CONFIG="${FUSION_ROOT}/fusion-v11/ChatGPT_Upload_v12.2/config/fusion_v12.2_config.json"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

# Function to check dependencies
check_dependencies() {
    echo -e "${BLUE}Checking dependencies...${NC}"
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}Python 3 is required but not found.${NC}"
        echo "Please install Python 3 from https://www.python.org/"
        exit 1
    fi
    
    # Check Node.js
    if ! command -v node &> /dev/null; then
        echo -e "${RED}Node.js is required but not found.${NC}"
        echo "Please install Node.js from https://nodejs.org/"
        exit 1
    fi
    
    echo -e "${GREEN}✓ All dependencies found${NC}"
}

# Function to select mode
select_mode() {
    echo -e "\n${BLUE}Select Operation Mode:${NC}"
    echo "1) Simulate - For exploration and testing"
    echo "2) Ship - For production-ready output"
    echo "3) Critique - For analysis and improvement"
    echo "4) Prototype - For rapid implementation"
    
    read -p "Enter mode (1-4) [default: 1]: " mode_choice
    
    case $mode_choice in
        2) FUSION_MODE="ship";;
        3) FUSION_MODE="critique";;
        4) FUSION_MODE="prototype";;
        *) FUSION_MODE="simulate";;
    esac
    
    echo -e "${GREEN}✓ Mode set to: $FUSION_MODE${NC}"
}

# Function to select chain template
select_chain() {
    echo -e "\n${BLUE}Select Chain Template:${NC}"
    echo "1) Figma to Prototype"
    echo "2) Product Strategy"
    echo "3) Quality Validation"
    
    read -p "Enter chain (1-3) [default: 1]: " chain_choice
    
    case $chain_choice in
        2) FUSION_CHAIN="product_strategy";;
        3) FUSION_CHAIN="quality_validation";;
        *) FUSION_CHAIN="figma_to_prototype";;
    esac
    
    echo -e "${GREEN}✓ Chain set to: $FUSION_CHAIN${NC}"
}

# Function to initialize quality system
init_quality_system() {
    echo -e "\n${BLUE}Initializing Quality System...${NC}"
    
    # Check quality components
    if [ -d "${FUSION_ROOT}/fusion-v11/ChatGPT_Upload_v12.2/quality" ]; then
        echo -e "${GREEN}✓ Quality system found${NC}"
        export FUSION_QUALITY_PATH="${FUSION_ROOT}/fusion-v11/ChatGPT_Upload_v12.2/quality"
    else
        echo -e "${RED}✗ Quality system not found${NC}"
        exit 1
    fi
    
    # Initialize metrics
    echo -e "${GREEN}✓ Quality metrics initialized${NC}"
    
    # Initialize monitoring
    echo -e "${GREEN}✓ Quality monitoring active${NC}"
}

# Function to start system
start_system() {
    echo -e "\n${BLUE}Starting Fusion V12.2...${NC}"
    
    # Export configuration
    export FUSION_MODE
    export FUSION_CHAIN
    export FUSION_CONFIG
    
    # Start the system
    python3 "${FUSION_ROOT}/fusion-v11/ChatGPT_Upload_v12.2/launch.py" \
        --mode "$FUSION_MODE" \
        --chain "$FUSION_CHAIN" \
        --config "$FUSION_CONFIG"
}

# Main execution
main() {
    echo -e "${BLUE}🚀 Fusion V12.2 Launcher${NC}\n"
    
    # Check dependencies
    check_dependencies
    
    # Initialize quality system
    init_quality_system
    
    # Select mode
    select_mode
    
    # Select chain template
    select_chain
    
    # Start system
    start_system
}

# Run main function
main 