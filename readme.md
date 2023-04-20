# Lifeman
A whole life manager to help keep track of common life chores. 

# Design
## Goals
1. Easily inventory the state your life
1. Track long term goals and changes
1. Automatically prioritize 100+ common goals

## User Experience
1. The user fills out a short quiz
2. The app prioritizes common goals based on the quiz
3. The app checks in weekly to synchronize goals and progress

## Technical Design

### Frontend
A basic CRUD app with a few graphs. 

1. Create a new Svelte project manually.
2. Install and configure Vite for building the project.
3. Use Svelte Kit to handle server-side rendering and routing.
4. Create a new component for each page of the app.
5. Use Fetch to make HTTP requests to the backend API.

### Backend
Sqlite with a job manager.

1. [X] Create a new Python project using virtualenv.
2. [X] Install and configure FastAPI for handling HTTP requests.
3. [X] Use SQLAlchemy to connect to a SQLite database.
4. [X] Use Celery to handle background tasks.
5. Deploy the backend to a Linux machine using Docker.

### Priority Levels

1. Survival
2. Security
3. Relationships
4. Esteem
5. Actualization
6. Other