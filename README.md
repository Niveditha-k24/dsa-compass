# dsa-compass

A backend that tracks how I solve DSA problems and recommends what to practice next.

## What it does

Most practice trackers only record whether a problem was solved. DSA Compass records
how each attempt went: time taken, how much help was needed, number of hints, number
of tries, and where I got stuck. It turns that into a score for each attempt using
simple, explainable rules, and uses the scores to recommend the next problem to
practice (an easier one, a similar one, or something new). The problem list follows
a roadmap such as NeetCode 150, which is stored as data so other roadmaps can be added.

## Planned tech stack

- **Python**: the programming language
- **FastAPI**: receives requests and sends back responses
- **PostgreSQL**: stores problems and attempts
- **SQLAlchemy**: lets Python work with the database
- **Alembic**: tracks changes to the database tables
- **Pydantic**: checks that incoming data is valid
- **Pytest**: automated tests
- **uv**: manages the project's Python packages

## How to run

1. Install the dependencies:

   ```bash
   uv sync
   ```

2. Start the server:

   ```bash
   uv run uvicorn main:app --reload
   ```

3. Open these in your browser:
   - http://127.0.0.1:8000/health shows `{"status":"ok"}`
   - http://127.0.0.1:8000/docs shows the Swagger page

To stop the server, press `Ctrl+C` in the terminal.
