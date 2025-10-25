# 🩺 Django Health Tracker

A web-based health tracking application built using **Python (Django Framework)**.  
It allows users to register, log in, and record their daily health metrics in a simple, user-friendly interface.

---

## 🚀 Features

- 👤 **User Authentication**
  - Register, login, and logout securely using Django’s built-in user system.
- 🩸 **Health Log Management**
  - Add, view, update, or delete daily health logs.
- 📅 **Date-based Record Filtering**
  - View health history sorted by most recent entries.
- 🎨 **Responsive UI**
  - Clean and minimal HTML/CSS design for desktop and mobile.
- 🔒 **User-specific Data**
  - Each user sees only their own logs (protected routes).

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Python, Django |
| Frontend | HTML5, CSS3, Bootstrap |
| Database | SQLite3 (default Django DB) |
| Version Control | Git & GitHub |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/swati-londhe/Health-Tracker.git
cd Health-Tracker
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On macOS/Linux
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Apply Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5️⃣ Run the Development Server
bash
Copy code
python manage.py runserver
Then open your browser and go to 👉 http://127.0.0.1:8000/

📂 Project Structure
csharp
Copy code
Health-Tracker/
│
├── health_tracker/        # Main Django app
├── templates/             # HTML templates
├── static/                # CSS and JS files
├── db.sqlite3             # Database file
├── manage.py              # Django management script
└── README.md              # Project documentation
🧑‍💻 Author
Swati Londhe
📧 swatilondhe2911@gmail.com
🌐 GitHub Profile

🌟 Future Enhancements
Add BMI calculation and visualization (charts)

Include reminders/notifications

Add REST API endpoints using Django REST Framework

Integrate with wearable device data (future scope)

