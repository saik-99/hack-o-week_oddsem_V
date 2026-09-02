# Student Records API (Hack-o-Week)

A simple yet powerful **REST API** for managing student records, built with **Flask**, validated with **Pydantic**, and stored in a local **SQLite** database. The project also includes a modern **glassmorphism-styled web dashboard** for intuitive CRUD operations without needing a frontend framework.

This project was developed as part of the **Hack-o-Week** event (Odd Semester V).

## 🚀 Features

- **Full CRUD Operations**: Create, Read, Update, and Delete student records seamlessly.
- **Robust Validation**: Uses **Pydantic** to ensure data integrity (e.g., valid ages, non-empty names) with clear error messages.
- **Persistent Storage**: Data is stored in **SQLite**, ensuring records survive server restarts.
- **Live Search & Filter**: The frontend dashboard allows real-time searching and filtering of students.
- **Modern UI**: A clean **glassmorphism** design built with plain HTML, CSS, and vanilla JavaScript.
- **Jupyter Notebooks**: Includes step-by-step notebooks (`hackoweek*.ipynb`) demonstrating the development process and API testing.

## 🛠 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python, Flask |
| **Validation** | Pydantic |
| **Database** | SQLite |
| **Frontend** | HTML, CSS, Vanilla JavaScript |
| **Development** | Jupyter Notebooks |

## 📂 Project Structure

```text
.
├── README.md
├── student_apihackoweek1-2.py   # Main Flask application entry point
├── database.py                  # SQLite database connection and setup
├── schemas.py                   # Pydantic models for request validation
├── templates/
│   └── index.html               # Glassmorphism web dashboard
├── students.db                  # SQLite database file (auto-created on first run)
├── studentinfo.html             # Legacy/Alternative HTML view
├── hckoweek3-4.ipynb            # Development notes: Weeks 3-4
├── hackoweekpython5-6.ipynb     # Development notes: Weeks 5-6
├── hackoweek7_8.ipynb           # Development notes: Weeks 7-8
└── hackoweek9_10.ipynb          # Development notes: Weeks 9-10
🏁 Getting Started
Prerequisites
Python 3.8+
pip package manager
Installation
Clone the repository:

bash

Copy
git clone https://github.com/saik-99/hack-o-week_oddsem_V.git
cd hack-o-week_oddsem_V
Create a virtual environment (recommended):

bash

Copy
python3 -m venv venv

# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
Install dependencies:

bash

Copy
pip install flask pydantic
Run the application:

bash

Copy
python3 student_apihackoweek1-2.py
Access the Dashboard: Open your browser and visit: http://localhost:5001

📡 API Reference
The API runs on http://localhost:5001.

GET
/students
List all students
GET
/students/<id>
Get a single student by ID
POST
/students
Create a new student
PUT
/students/<id>
Update an existing student
DELETE
/students/<id>
Delete a student
Example Requests
Create a new student:

bash

Copy
curl -X POST http://localhost:5001/students \
  -H "Content-Type: application/json" \
  -d '{"name": "Ali Khan", "age": 20, "grade": "A", "course": "Computer Science"}'
Update a student's grade:

bash

Copy
curl -X PUT http://localhost:5001/students/1 \
  -H "Content-Type: application/json" \
  -d '{"grade": "A+"}'
Delete a student:

bash

Copy
curl -X DELETE http://localhost:5001/students/1
Example Response
json

Copy
{
  "id": 1,
  "name": "Ali Khan",
  "age": 20,
  "grade": "A",
  "course": "Computer Science"
}
📋 Validation Rules
The API enforces the following rules via Pydantic:

name
string
Yes
Non-empty string
age
integer
No
Between 0 and 120
grade
string
No
Any string
course
string
No
Any string
Invalid requests will return a 400 Bad Request status with details on the validation failure.

🗺 Roadmap

 Add authentication for write operations (POST/PUT/DELETE)

 Implement pagination for large student lists

 Add query parameter filtering (e.g., /students?course=Math)

 Add Docker support for containerized deployment
📄 License
This project is licensed under the MIT License.

👨‍💻 Author
saik-99
Hack-o-Week Odd Semester V Participant
