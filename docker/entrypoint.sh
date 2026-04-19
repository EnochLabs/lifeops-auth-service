#!/bin/sh

set -e

# Extract host and port from MONGODB_URL
# This is a simple way to wait for MongoDB. In a more complex setup,
# you might want to use a tool like 'wait-for-it' or 'docker-compose-wait'.
# For now, we'll just try to reach the service if possible.

echo "Starting LifeOps Auth Service..."

# You can add migration commands here if needed in the future
# e.g., python scripts/migrate.py

# Execute the main command
exec "$@"
