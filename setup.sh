#!/bin/bash

cd /app

# create venv if it doesn't exist
if [ ! -d "venv" ]; then
    python -m venv venv
fi

# activate venv
source venv/bin/activate

# install requirements
pip install --upgrade pip
pip install -r requirements.txt

# run bot
python disc_svullo.py