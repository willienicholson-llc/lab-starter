"""Starter service for the technical conversation.

One endpoint, one page, one test, one CI step. The task is given live.
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Lab starter")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return """<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Lab starter</title></head>
<body style="font-family: sans-serif; max-width: 40rem; margin: 3rem auto;">
  <h1>Lab starter</h1>
  <p>The service is running. Check <a href="/health">/health</a> and <a href="/docs">/docs</a>.</p>
</body>
</html>"""
