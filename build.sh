#!/usr/bin/env bash
# exit on error

sudo apt install mecab -y
sudo apt install libmecab-dev -y
sudo apt install mecab-ipadic-utf8 -y

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate