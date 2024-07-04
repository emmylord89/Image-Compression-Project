#!/bin/bash
source venv/bin/activate  # Activate your virtual environment
exec gunicorn -c gunicorn_config.py app:app
