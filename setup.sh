#!/bin/bash
set -euo pipefail

# Create a new Python project using virtualenv
python3 -m venv myproject
source myproject/bin/activate

# Install FastAPI
pip install fastapi uvicorn sqlalchemy

# Create a main.py file with FastAPI code
echo "from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World!'}" > main.py

# Run the server with uvicorn
uvicorn main:app --reload