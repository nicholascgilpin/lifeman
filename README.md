# lifeman
A tool for prioritizing all the big and small things in life, so that you don't lose focus on what's important. 

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

Backend
- CRUD
- Task Scheduler
- Database: Sqlite
