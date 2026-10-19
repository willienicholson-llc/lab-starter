# Lab starter

A small FastAPI service used for a live technical conversation. The task itself is given on the call.

## What is here

- `app/main.py`: the service, 2 routes (`/` and `/health`)
- `tests/test_health.py`: 2 passing tests
- `.github/workflows/ci.yml`: runs the tests on every push

## Before the call

1. Fork this repository to your own GitHub account.
2. Clone your fork and check it runs:

```bash
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload
```

3. Open `http://127.0.0.1:8000` and confirm the page loads.
4. Check that the CI run on your fork is green (Actions tab).

Have Claude Code or Cursor signed in and ready to screen-share. No API keys are needed for the exercise.
