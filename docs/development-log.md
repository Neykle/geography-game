\# Development Log



\## Phase 1 - Project Setup

\*\*Dates:\*\* 12–15 September 2026



\### Goal

Set up the basic development environment and create a working foundation for my geography game.



\### What I completed

\- Installed and configured Git, Node.js and npm.

\- Checked my existing Python installation and decided to continue using Python 3.11.

\- Created a GitHub repository for the project.

\- Created the initial project structure with separate `backend`, `frontend`, and `data` folders.

\- Created a basic Flask backend server in Python.

\- Created a basic React frontend using Vite.

\- Ran both the frontend and backend locally.

\- Connected React to Flask and successfully displayed data returned by the Flask API in React.

\- Created a basic SQLite database and a `countries` table.

\- Added a script that can create the database automatically.



\### Problems I encountered

\- PowerShell initially blocked npm scripts because of its execution policy.

\- Git was not immediately recognized after installation and required restarting PowerShell.

\- I accidentally ran some paths as commands instead of using `cd`.

\- Vite did not work properly when I tried running it through PowerShell ISE, so I switched to regular PowerShell.

\- React initially could not communicate with Flask because of CORS. I solved this by adding `flask-cors` to the backend.



\### What I learned

\- The basic roles of React, Flask and SQLite in a web application.

\- How a frontend and backend can run separately and communicate using HTTP requests.

\- How to use basic Git commands such as `add`, `commit`, `push`, `clone` and `status`.

\- How Python virtual environments are used to keep project dependencies separate.

\- What CORS is and why it can prevent a frontend from accessing a backend running on a different port.

\- How SQLite databases and tables can be created using Python.



\### Current project structure

\- `backend/` — Flask API and database code

\- `frontend/` — React application

\- `data/` — future geography datasets/import scripts

\- `docs/` — development documentation



\### Next

Start Phase 2 and begin developing the actual geography game rather than just its technical foundation.




## Phase 2 — Database and Country Data

### Goal
Create a working country database and connect it to the frontend.

### What I completed
- Created a test list of North American countries.
- Researched data sources for the 9 game categories.
- Added a `country_stats` table to SQLite.
- Imported countries from CSV using Python.
- Imported test country rankings into SQLite.
- Checked the database for missing data.
- Created a Flask API endpoint that returns a random country.
- Connected React to the Flask API.
- Displayed country ranks in the frontend.

### Problems I encountered
- Created the `country_stats.csv` file inside an extra `data` folder by mistake.
- Flask was not found because the Python virtual environment was not activated.
- Learned how to fix file paths and activate the virtual environment.

### What I learned
- How CSV data can be imported into SQLite with Python.
- How two database tables can be linked using a foreign key.
- How Flask reads data from SQLite and returns JSON.
- How React fetches JSON from a Flask API.
- How backend data reaches the frontend.

### Next
Start Phase 3 and build the actual 3×3 game interface and game logic.