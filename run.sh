set -e

# Default configuration assumes production
MODE=production
USE_SSL=1
LOG_LEVEL=WARNING
UVICORN_LOG_LEVEL=warning
RELOAD=""
ACCESS_LOG="--no-access-log"

while [ $# -gt 0 ]; do
  case "$1" in
    -test|--test)
      echo "Running in test mode..."
      MODE=test
      USE_SSL=0
      LOG_LEVEL=DEBUG
      UVICORN_LOG_LEVEL=debug
      RELOAD="--reload"
      ACCESS_LOG=""
      shift
      ;;
    -production|--production)
      MODE=production
      USE_SSL=1
      LOG_LEVEL=WARNING
      UVICORN_LOG_LEVEL=warning
      RELOAD=""
      ACCESS_LOG="--no-access-log"
      shift
      ;;
    *)
      echo "Usage: $0 [-test|--test|-production|--production]" >&2
      exit 1
      ;;
  esac
done

export LOG_LEVEL
if [ "$MODE" = test ]; then
  set -x
else
  set +x
fi

if [ "$USE_SSL" -eq 1 ]; then
  export SSL_CERTFILE=certifications/velox.crt
  export SSL_KEYFILE=certifications/velox.key
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
      $RELOAD --host 0.0.0.0 --port "$PORT" \
      --log-level "$UVICORN_LOG_LEVEL" $ACCESS_LOG \
      --ssl-certfile "$SSL_CERTFILE" --ssl-keyfile "$SSL_KEYFILE" \
      > "$LOGFILE" 2>&1 &
else
  nohup python3 -u -m uvicorn backend.src.main.API.api:app \
      $RELOAD --host 0.0.0.0 --port "$PORT" \
      --log-level "$UVICORN_LOG_LEVEL" $ACCESS_LOG \
      > "$LOGFILE" 2>&1 &
  echo "!!! WARNING: INSECURE !!!"
fi

echo "API started (pid $!) and logging to $LOGFILE"
