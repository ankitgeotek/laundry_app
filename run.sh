#!/bin/bash

# Navigate to the backend directory
cd "$(dirname "$0")/backend"

# Activate the virtual environment
source lib/.venv/bin/activate

# kill the already existing port
sudo lsof -i :8000

# Run the FastAPI application with Uvicorn
uvicorn app.main:app --reload
