#!/bin/bash

cd /app

# clone if not exists
if [ ! -d ".git" ]; then
    git clone https://github.com/jedifindtrick/svullo-bot.git .
else
    git pull origin main
fi

if [ ! -d "venv" ]; then
    python -m venv venv
fi

source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python disc_svullo.py