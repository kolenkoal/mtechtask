#!/bin/bash

set -e

psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f /app/scripts/db.sql

exec "$@"
