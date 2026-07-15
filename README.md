# Student Records API

A simple REST API for managing student records, built with **Flask**, validated with **Pydantic**, and stored in a local **SQLite** database. Includes a glassmorphism-styled web dashboard for viewing, adding, editing, and deleting students.

## Features

- Full CRUD (Create, Read, Update, Delete) for student records
- Request validation with Pydantic — rejects bad data (missing names, invalid ages) with clear error messages
- Persistent storage using SQLite — data survives server restarts
- Live search/filter on the frontend
- Clean glassmorphism UI with subtle animations, built with plain HTML/CSS/JS (no frontend framework required)

## Tech stack

| Layer | Tool |
|---|---|
| Backend | Python, Flask |
| Validation | Pydantic |
| Database | SQLite |
| Frontend | HTML, CSS, vanilla JavaScript |

## Project structure

```
.
├── student_api.py       # Flask app: routes and request handling
├── database.py          # SQLite connection and table setup
├── schemas.py           # Pydantic models for request validation
├── templates/
│   └── index.html       # Frontend dashboard
└── students.db          # SQLite database file (auto-created on first run)
```

## Getting started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/student-api.git
cd student-api
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask pydantic
```

### 4. Run the app

```bash
python3 student_api.py
```

### 5. Open it

Visit **http://localhost:5001** in your browser for the dashboard, or hit the API directly (see below).

## API reference

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | List all students |
| GET | `/students/<id>` | Get a single student by ID |
| POST | `/students` | Create a new student |
| PUT | `/students/<id>` | Update an existing student |
| DELETE | `/students/<id>` | Delete a student |

### Example requests

**Create a student**
```bash
curl -X POST http://localhost:5001/students \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "age": 22, "grade": "A", "course": "Math"}'
```

**Update a student's grade**
```bash
curl -X PUT http://localhost:5001/students/1 \
  -H "Content-Type: application/json" \
  -d '{"grade": "A+"}'
```

**Delete a student**
```bash
curl -X DELETE http://localhost:5001/students/1
```

### Example response

```json
{
  "id": 1,
  "name": "Ali Khan",
  "age": 20,
  "grade": "A",
  "course": "Computer Science"
}
```

## Validation rules

- `name` — required, non-empty string
- `age` — optional, integer between 0 and 120
- `grade` — optional string
- `course` — optional string

Invalid requests return a `400` status with details on what failed.

## Roadmap

- [ ] Authentication for write operations
- [ ] Pagination for large student lists
- [ ] Filter/search via query parameters (e.g. `/students?course=Math`)
- [ ] Docker support

## License

MIT
