#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies using uv
uv sync

# Convert static files (CSS, Images) for production
uv run python manage.py collectstatic --no-input

# Run database migrations
uv run python manage.py migrate