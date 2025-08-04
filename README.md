# AI Training Plans
This project focuses on artificially generating training plans for the 5k/10k distances across Intermediate and Advanced experience levels. Project was began in June 2025.

## Mobile API Configuration

The iOS client expects a `mobile/TrainingPlan/Resources/APIConfig.plist` file
containing an `API_BASE_URL` key pointing at your backend server. Copy the
provided `APIConfig.plist.example` to `APIConfig.plist` and edit the URL to
match your environment. The value can also be overridden with the
`API_BASE_URL` environment variable at runtime.

## Backend Database Configuration

The backend expects a `backend/src/utils/SQLutils/config.py` file defining a
`DB_CREDENTIALS` dictionary with the database connection details. Copy the
provided `config.py.example` to `config.py` and fill in your `DB_USERNAME`,
`DB_PASSWORD`, and database `host` values so the application can connect to
your PostgreSQL instance.
