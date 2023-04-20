# lifeman
A tool for prioritizing all the big and small things in life, so that you don't lose focus on what's important. 

## Schedule
To be implemented with free time that I don't have. ETA: 2035

## Design

### User Experience
New User Workflow
1. The user answers a 20 question quiz about their life
2. The life manager displays a detailed quality of life rating
3. The life manager creates a prioritized list of life improvment tasks

Existing User Workflow
1. The life manager checks in weekly to monitor how the user is doing
2. The life manager records changes in life quality
3. The list of life improvment tasks is updated

Life Quality Rating
- A person's quality of life is rated higher if it meets more of Maslov's Hierarchy of needs. 
- A person's needs are prioritized via Maslov's Hierarchy with adjustments for the user's age.
  1. Survival Needs
  2. Security  Needs
  3. Social Needs
  4. Esteem Needs
  5. Self-Actualization Needs
 - Additionally, these needs are further subdivided into 4 categories: Happiness, Health, Wealth, and Wisdom with the following meanings:
    1. Happiness - Are they satisfied with this need?
    2. Health - Are they going to lose fulfillment of this need in the next year?
    3. Wealth - To what degree is this need fufilled compared to the minimum degree?
    4. Wisdom - Does the person have suffecient knowledge to fufill this need?

Task Generation
- A common set of goals will be included
- Secure Financial Health Example: Save up enough money to cover one month of expenses.
- Social Family Wisdom Example: Update the addresses of all your immediate family members.

### Technical Design
Frontend
- Chat Interface with graph summary diagram
- questions messaged to the user on a schedule

Todo:
1. Create a new Svelte project manually.
2. Install and configure Vite for building the project.
3. Use Svelte Kit to handle server-side rendering and routing.
4. Create a new component for each page of the app.
5. Use Fetch to make HTTP requests to the backend API.

Backend
- CRUD
- Task Scheduler
- Database: Sqlite

Todo:
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