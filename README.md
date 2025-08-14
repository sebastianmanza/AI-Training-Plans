# AI Training Plans
This project focuses on artificially generating training plans for the 5k/10k distances across Intermediate and Advanced experience levels. Project was began in June 2025.

## First-Time Setup

If you're getting started with the project for the first time, follow these steps:

1. **Install backend dependencies**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements/base.txt
   ```

2. **Create environment files**

   ```bash
   cp .env.example .env
   cp mobile/TrainingPlan/Resources/APIConfig.plist.example mobile/TrainingPlan/Resources/APIConfig.plist
   ```

   Update `.env` and `APIConfig.plist` to match your environment (see sections below for details).

3. **Run the backend**

   ```bash
   ./run.sh -production   # HTTPS with minimal logging
   ./run.sh -test         # HTTP, auto-reload, debug logging
   ```

   Omitting the flag defaults to production mode.

4. **Verify the setup** (optional)

   ```bash
   pytest
   ```

### Windows (PowerShell) equivalents

If you're developing on Windows, use PowerShell with these commands:

```powershell
python -m venv .venv
.\venv\Scripts\Activate.ps1
./run.ps1 -production   # HTTPS with minimal logging
./run.ps1 -test         # HTTP, auto-reload, debug logging
```

PowerShell uses backslashes (`\`) for paths, and you can invoke scripts in the current directory with `./`. The `python` command replaces `python3` on Windows.

## Mobile API Configuration

The iOS client expects a `mobile/TrainingPlan/Resources/APIConfig.plist` file
containing an `API_BASE_URL` key pointing at your backend server. Copy the
provided `APIConfig.plist.example` to `APIConfig.plist` and edit the URL to
match your environment. The value can also be overridden with the
`API_BASE_URL` environment variable at runtime. When testing from a physical
device, use your machine's LAN IP (for example,
`http://192.168.1.10:8000`) rather than `http://localhost:8000` so both devices
can reach the server.

## Backend Database Configuration

Database credentials are loaded from environment variables defined in the
project's `.env` file. The `backend/config.py` module uses `pydantic` to read
`DB_USERNAME`, `DB_PASSWORD`, and `DB_HOST` values and makes them available
through the `DB_CREDENTIALS` dictionary. A `SECRET_KEY` is also read from the
environment for signing authentication tokens; ensure this value is set before
running the API.
