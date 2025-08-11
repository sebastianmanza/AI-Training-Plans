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

2. **Create required config files**

   ```bash
   cp mobile/TrainingPlan/Resources/APIConfig.plist.example mobile/TrainingPlan/Resources/APIConfig.plist
   cp backend/src/utils/SQLutils/config.py.example backend/src/utils/SQLutils/config.py
   ```

   Edit the copied files to match your environment (see sections below for details).

3. **Run the backend**

   ```bash
   ./run.sh           # uses HTTPS
   ./run.sh --http    # run without SSL for local testing
   ```

4. **Verify the setup** (optional)

   ```bash
   pytest
   ```

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

The backend expects a `backend/src/utils/SQLutils/config.py` file defining a
`DB_CREDENTIALS` dictionary with the database connection details. Copy the
provided `config.py.example` to `config.py` and fill in your `DB_USERNAME`,
`DB_PASSWORD`, and database `host` values so the application can connect to
your PostgreSQL instance.
