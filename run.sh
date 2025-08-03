set -e

LOGFILE="$(pwd)/logs/uvicorn.log"
PORT=${PORT:-8000}

# Terminate any process using the target port
lsof -tiTCP:$PORT -sTCP:LISTEN | xargs kill -9 2>/dev/null || true

sleep 0.2

echo "Starting FastAPI backend on port $PORT..."

SSL_CERTFILE=${SSL_CERTFILE:-}
SSL_KEYFILE=${SSL_KEYFILE:-}
SSL_ARGS=""
if [ -n "$SSL_CERTFILE" ] && [ -n "$SSL_KEYFILE" ]; then
  SSL_ARGS="--ssl-certfile $SSL_CERTFILE --ssl-keyfile $SSL_KEYFILE"
fi

mkdir -p "$(dirname "$LOGFILE")"
nohup python3 -u -m uvicorn backend.src.main.API.api:app \
    --reload --host 0.0.0.0 --port "$PORT" $SSL_ARGS \
    > "$LOGFILE" 2>&1 &

echo "API started (pid $!) and logging to $LOGFILE"
