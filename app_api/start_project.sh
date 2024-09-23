#!/bin/bash
pip install fastapi uvicorn asyncpg sqlalchemy aiosqlite
python -m uvicorn main:app --host 127.0.0.1 --port 8060 --reload
