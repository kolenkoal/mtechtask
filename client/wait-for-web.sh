#!/bin/bash

web_url="http://web:8000/api/data/"

check_web_service() {
    echo "Checking if the web service is available..."
    until curl -sSf $web_url > /dev/null; do
        echo "Web service is not available yet. Retrying..."
        sleep 3
    done
    echo "Web service is available!"
}

check_web_service

echo "Starting the client service..."

python main.py