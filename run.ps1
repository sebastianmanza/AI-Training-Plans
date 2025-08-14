param(
    [switch]$Test,
    [switch]$Production
)

$MODE = "production"
$USE_SSL = $true
$LOG_LEVEL = "WARNING"
$UVICORN_LOG_LEVEL = "warning"
$RELOAD = ""
$ACCESS_LOG = "--no-access-log"

if ($Test) {
    Write-Host "Running in test mode..."
    $MODE = "test"
    $USE_SSL = $false
    $LOG_LEVEL = "DEBUG"
    $UVICORN_LOG_LEVEL = "debug"
    $RELOAD = "--reload"
    $ACCESS_LOG = ""
} elseif ($Production) {
    # defaults, do nothing
} elseif ($PSBoundParameters.Count -gt 0) {
    Write-Host "Usage: .\\run.ps1 [-Test | -Production]" -ForegroundColor Red
    exit 1
}

$env:LOG_LEVEL = $LOG_LEVEL
if ($MODE -eq "test") {
    $DebugPreference = "Continue"
} else {
    $DebugPreference = "SilentlyContinue"
}

if ($USE_SSL) {
    $env:SSL_CERTFILE = "certifications/endorphin.crt"
    $env:SSL_KEYFILE = "certifications/endorphin.key"
}

$LOGFILE = Join-Path (Get-Location) "logs/uvicorn.log"
$PORT = $env:PORT
if (-not $PORT) { $PORT = 8000 }

# Terminate any process using the target port
try {
    Get-NetTCPConnection -LocalPort $PORT -State Listen -ErrorAction Stop |
        Select-Object -First 1 |
        ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
} catch { }

Start-Sleep -Milliseconds 200

Write-Host "Starting FastAPI backend on port $PORT..."

if ($USE_SSL -and (-not $env:SSL_CERTFILE -or -not $env:SSL_KEYFILE)) {
    Write-Host "SSL_CERTFILE and SSL_KEYFILE must be set for HTTPS connections." -ForegroundColor Red
    exit 1
}

$logDir = Split-Path $LOGFILE
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$cmd = "python -u -m uvicorn backend.src.main.API.api:app $RELOAD --host 0.0.0.0 --port $PORT --log-level $UVICORN_LOG_LEVEL $ACCESS_LOG"
if ($USE_SSL) {
    $cmd += " --ssl-certfile `"$env:SSL_CERTFILE`" --ssl-keyfile `"$env:SSL_KEYFILE`""
}

$process = Start-Process -FilePath "cmd.exe" -ArgumentList "/c $cmd >> `"$LOGFILE`" 2>>&1" -NoNewWindow -PassThru

if (-not $USE_SSL) {
    Write-Warning "!!! WARNING: INSECURE !!!"
}

Write-Host "API started (cmd.exe pid $($process.Id)) and logging to $LOGFILE"
Write-Host "Use `"Get-Process -Name python | Select-Object -Last 1`" if the Python PID is required."
