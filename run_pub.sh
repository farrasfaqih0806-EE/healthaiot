#!/bin/bash
cd ~/HealthAIoT/Raspberry
source venv/bin/activate
export PYTHONPATH=.
python mqtt/publisher.py

