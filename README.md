<img width="1024" height="346" alt="taskflow-logo-transparent2" src="https://github.com/user-attachments/assets/02b5ee55-e990-420a-9c75-e25b1533e92b" />

# TaskFlow #

**TaskFlow** is a gamified productivity web application inspired by the famous anime and manhwa **Solo Leveling**, it is built with Django. It transforms daily tasks and projects into quests, allowing users to earn XP, achieve ranks, and unlock achievements as they complete goals. Designed to improve motivation and consistency, TaskFlow blends productivity with a sense of progression similar to games.

## Features ##

- User Authentication: Sign up, log in, and manage profiles securely.

- Quests & Tasks: Create quests (projects) and add multiple tasks under each quest.

- Gamification System: Earn XP for completing tasks and progress through ranks, E to S.

- Rank Progression: Dynamic rank updates based on total XP.

- Achievements (Coming Soon): Unlock milestones and badges as you progress.

- Responsive Dashboard: View quests, progress bars, XP, and ranks all in one place.

- Profile Page: Personalized profile with XP tracking and rank display.

## Rank System ##
Rank Title	                  
- **E-RANK ROOKIE: AWAKENED HUNTER**       0 – 499
- **D-RANK NOVICE: MANA HUNTER**	     500 – 1999
- **C-RANK ADEPT: APEX HUNTER**	      2000 – 3999
- **B-RANK EXPERT: THE PHANTOM HUNTER**	       4000 – 7999
- **A-RANK ELITE: ELITE HUNTER**	8000 – 14999
- **S-RANK MASTER: THE SHADOW MONARCH**	      15000+
## ERD ##
![image](https://git.generalassemb.ly/mousaaricat/FlowQuest-Capstone/assets/55686/d9d8b0b2-defb-4290-b4cc-8d3b446619cf)

## The Stack ##

Backend: **Django (Python)**

Frontend: **HTML, CSS**

Database: **PostgreSQL**

Deployment: **Render**

Authentication: **Django Authentication**

## Future Enhancements ##

 - Add badges and achievements  system

 - Introduce leaderboards and social features

 - Add Daily Streaks

 - Add notifications and reminders

 - Enable progress analytics and reports

## Setup & Installation ##
### 1. Clone the Repository ###
```bash
git clone https://github.com/<your-username>/TaskFlow.git
cd TaskFlow
```

### 2. Create and Activate a Virtual Environment ### 
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies ###
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables ###
```bash
cp .env.example .env
```
### 5. Apply Migrations ###
```bash
python manage.py migrate
```

### 6. Run the Development Server ###
```bash
python manage.py runserver
```

Now open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to view the app.

## Entry Point ##
The main entry point for the project is:
```bash
FlowQuest/manage.py
```

## Environment Variables ##
You’ll need a ```bash .env ``` file with these variables for local development:
```bash
# Django
SECRET_KEY=your_django_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database (Local)
DB_NAME=taskflow_db
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432

# For Production (optional)
DATABASE_URL=your_render_database_url
```


## Database ##

- Default: PostgreSQL
- Local config: loaded from .env
- Production config: automatically uses DATABASE_URL if set


## Special Requirements ##
- Python 3.9+
- PostgreSQL installed locally
- Django 5.x
- dj-database-url and python-dotenv must be installed


## Contributing ##
Contributions are welcome!
Before submitting a pull request:

1- Fork the repository
2- Create a new branch
3- Commit your changes with clear messages
4- Open a pull request

### Note: Some of the css animations and design were taken from the open source css website: https://uiverse.io/ ###
