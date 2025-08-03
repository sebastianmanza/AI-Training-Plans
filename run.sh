set -e
# Set a local SSL: during production we will need to upgrade and get a certificate
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout key.pem -out cert.pem
export SSL_CERTFILE=/absolute/path/cert.pem
export SSL_KEYFILE=/absolute/path/key.pem

LOGFILE="$(pwd)/logs/uvicorn.log"
PORT=${PORT:-8000}

# Terminate any process using the target port
lsof -tiTCP:$PORT -sTCP:LISTEN | xargs kill -9 2>/dev/null || true

sleep 0.2

echo "Starting FastAPI backend on port $PORT..."

SSL_CERTFILE=${SSL_CERTFILE:-}
SSL_KEYFILE=${SSL_KEYFILE:-}

if [ -z "$SSL_CERTFILE" ] || [ -z "$SSL_KEYFILE" ]; then
  echo "SSL_CERTFILE and SSL_KEYFILE must be set for HTTPS connections." >&2
  exit 1
fi

mkdir -p "$(dirname "$LOGFILE")"
nohup python3 -u -m uvicorn backend.src.main.API.api:app \
    --reload --host 0.0.0.0 --port "$PORT" \
    --ssl-certfile "$SSL_CERTFILE" --ssl-keyfile "$SSL_KEYFILE" \
    > "$LOGFILE" 2>&1 &

echo "API started (pid $!) and logging to $LOGFILE"
