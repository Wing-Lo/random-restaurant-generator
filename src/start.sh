#!/bin/bash

install_python3() {
    echo "Attempting to install Python 3..."
    if [[ -x "$(command -v apt-get)" ]]; then
        sudo apt-get update
        sudo apt-get install python3 python3-venv python3-pip
    elif [[ -x "$(command -v brew)" ]]; then
        brew install python3
    elif [[ -x "$(command -v yum)" ]]; then
        sudo yum update
        sudo yum install python3
    else
        echo "Package manager not found. Please install Python 3 manually."
        exit 1
    fi
}

cd ./src

if ! [[ -x "$(command -v python3)" ]]; then
    echo "Python 3 is not installed. Trying to install..."
    install_python3
fi

pyv="$(python3 -V 2>&1)"
echo "Detected Python version: $pyv"

if [[ $pyv == "Python 3"* ]]; then
    python3 -m venv .venv 
    source .venv/bin/activate
    python3 main.py
else
    echo "Detected Python version is not sufficient."
    install_python3
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]; then
        python3 -m venv .venv 
        source .venv/bin/activate
        python3 main.py
    else
        echo "Python 3 installation failed. Please install it manually." >&2
        exit 1
    fi
fi