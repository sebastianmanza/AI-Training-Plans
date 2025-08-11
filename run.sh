set -e

USE_SSL=1
while [ $# -gt 0 ]; do
  case "$1" in
    -test|--http)
      USE_SSL=0
      shift
      ;;
    *)
      shift
      ;;
  esac
done

if [ "$USE_SSL" -eq 1 ]; then
  export SSL_CERTFILE=certifications/endorphin.crt
  export SSL_KEYFILE=certifications/endorphin.key
fi

LOGFILE="$(pwd)/logs/uvicorn.log"
PORT=${PORT:-8000}

# Terminate any process using the target port
lsof -tiTCP:$PORT -sTCP:LISTEN | xargs kill -9 || true

sleep 0.2

echo "Starting FastAPI backend on port $PORT..."

if [ "$USE_SSL" -eq 1 ]; then
  SSL_CERTFILE=${SSL_CERTFILE:-}
  SSL_KEYFILE=${SSL_KEYFILE:-}

  if [ -z "$SSL_CERTFILE" ] || [ -z "$SSL_KEYFILE" ]; then
    echo "SSL_CERTFILE and SSL_KEYFILE must be set for HTTPS connections." >&2
    exit 1
  fi
fi

mkdir -p "$(dirname "$LOGFILE")"
if [ "$USE_SSL" -eq 1 ]; then
  nohup python3 -u -m uvicorn backend.src.main.API.api:app \
      --reload --host 0.0.0.0 --port "$PORT" \
      --ssl-certfile "$SSL_CERTFILE" --ssl-keyfile "$SSL_KEYFILE" \
      > "$LOGFILE" 2>&1 &
else
  nohup python3 -u -m uvicorn backend.src.main.API.api:app \
      --reload --host 0.0.0.0 --port "$PORT" \
      > "$LOGFILE" 2>&1 &
fi

echo "API started (pid $!) and logging to $LOGFILE"
