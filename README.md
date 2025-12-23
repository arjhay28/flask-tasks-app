# TaskMate 🗂️

**TaskMate** is a web-based task management application built with **Flask**, designed to help users efficiently create, track, and manage tasks using predefined priority and status constraints.  
It uses **SQLAlchemy** as the ORM, **PostgreSQL** as the database, and **uv** as the package manager.

---

## 🚀 Features

- 📝 Create, edit, view, and delete tasks
- 🎯 Task priority enforcement:
  - `low`
  - `moderate`
  - `high`
  - `immediate`
- 📌 Task status tracking:
  - `pending`
  - `in-progress`
  - `completed`
  - `archived`
- 🧩 Data validation using Enum constraints
- 🗄️ PostgreSQL-backed persistent storage
- 🎨 Server-rendered UI using Jinja2 templates
- ⚡ Fast dependency management with **uv**

---

## 🛠️ Tech Stack

| Technology     | Purpose |
|----------------|---------|
| **Flask**      | Web framework |
| **SQLAlchemy** | ORM |
| **PostgreSQL** | Database |
| **Jinja2**     | Templating engine |
| **SCSS / CSS** | Styling |
| **uv**         | Python package manager |
| **Python**     | Backend language |

---

## 📁 Project Structure

```text
TASKS/
├── static/
│   ├── styles.css
│   ├── styles.css.map
│   └── styles.scss
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── create_task.html
│   ├── edit_task.html
│   ├── view_task.html
│   └── error.html
├── .env
├── .gitignore
├── .python-version
├── app.py
├── database.py
├── enums.py
├── models.py
├── routes.py
├── pyproject.toml
├── uv.lock
└── README.md


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/taskmate.git
cd taskmate

2️⃣ Install Dependencies (using uv)
uv sync

3️⃣ Environment Variables

Create a .env file in the project root:

DATABASE_URL=postgresql://username:password@localhost:5432/taskmate_db
SECRET_KEY=your_secret_key
FLASK_ENV=development

4️⃣ Initialize the Database

Make sure PostgreSQL is running and the database exists, then run:

uv run python database.py


(or your database initialization logic if handled elsewhere)

5️⃣ Run the Application
uv run python app.py


Visit the app at:

http://127.0.0.1:5000

🧠 Core Components
models.py

Defines the Task model using SQLAlchemy, including priority and status constraints.

enums.py

Contains Enum definitions for:

Priority

Status

routes.py

Handles application routes and business logic.

database.py

Manages database configuration and SQLAlchemy setup.

📊 Task Constraints
Priority
low | moderate | high | immediate

Status
pending | in-progress | completed | archived


These constraints ensure data integrity and consistent task lifecycle management.

🧪 Future Enhancements

🔐 User authentication

📅 Due dates & reminders

🔍 Task filtering and search

📱 Responsive UI improvements

📊 Task analytics dashboard

🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

📄 License

This project is licensed under the MIT License.

👤 Author

Arjhay De Chavez
TaskMate — A Flask-based task management application.

⭐ If you find this project useful, consider starring the repository!
