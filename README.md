# DeSo Media Bot

A bot that posts random images on DeSo. This bot will choose a random image from the images folder, post it on DeSo and delete it from the folder.

## How to run?

Clone the repository. Then create a Python virtual environment and then install dependencies

```bash
# Creating a virtual environment
python -m venv .venv
# Running virtual environment
source .venv/bin/activate
# Installing dependencies
pip install -r requirements.txt
```

Create a .env file in the root folder or set the following environment variables
```
public_key
seed_hex
```

To run it:
```bash
python app.py
```