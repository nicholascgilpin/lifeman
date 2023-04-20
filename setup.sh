#!/bin/bash
set -euo pipefail

# Create a new Python project using virtualenv
python3 -m venv myproject
source myproject/bin/activate

echo ""
echo "Installing run dependencies..."
if ! which redis-server &> /dev/null; then
    sudo apt install redis-server
fi
pip install fastapi uvicorn sqlalchemy celery redis

echo ""
echo "Installing test dependencies..."
pip install httpx

echo ""
echo "Starting Backend..."
echo "1/3"
redis-server &
REDIS_PID=$!
echo "2/3"
celery -A tasks worker --loglevel=info &
CELERY_PID=$!
echo "3/3"
uvicorn main:app --reload &
UVICORN_PID=$!

echo ""
echo "Waiting to kill running processes..."
echo ""

trap "kill $REDIS_PID $CELERY_PID $UVICORN_PID" EXIT

wait