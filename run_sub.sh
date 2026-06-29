#!/bin/bash
cd ~/HealthAIoT/Raspberry
source venv/bin/activate
export PYTHONPATH=.
python mqtt/mqtt_client.py

