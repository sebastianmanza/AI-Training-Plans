set -e

LOGFILE="$(pwd)/logs/uvicorn.log"
PORT=8000

# pkill -f "uvicorn.*api:app" 2>/dev/null || true

lsof -tiTCP:8000 -sTCP:LISTEN | xargs kill -9 || true

sleep 0.2
echo "Starting FastAPI backend..."
mkdir -p "$(dirname "$LOGFILE")"
nohup python3 -u -m uvicorn backend.src.main.API.api:app \
    --reload --host 0.0.0.0 --port 8000 \
    > "$LOGFILE" 2>&1 &
echo "API started (pid $!) and logging to "$LOGFILE""