
# Clean Architecture FastAPI Project

## Features
- BaseWorker abstraction
- ProcessWorker (ProcessPool - 4 workers)
- AsyncWorker (asyncio)
- Strategy pattern (easy switch)
- Clean modular structure

## Run
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py

## Switch Mode
set WORKER_MODE=async
