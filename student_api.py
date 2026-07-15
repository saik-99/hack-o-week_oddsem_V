from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


# Serves the frontend page (templates/index.html)
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# This is our "database" — just a list in memory (resets when server restarts)
students = [
    {"id": 1, "name": "Ali Khan", "age": 20, "grade": "A", "course": "Computer Science"},
    {"id": 2, "name": "Sara Ahmed", "age": 21, "grade": "B", "course": "Business"},
]


# GET /students -> show all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students), 200


# GET /students/<id> -> show one student
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200


# POST /students -> add a new student
@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Please provide at least a 'name' field"}), 400

    new_id = students[-1]["id"] + 1 if students else 1
    new_student = {
        "id": new_id,
        "name": data["name"],
        "age": data.get("age"),
        "grade": data.get("grade"),
        "course": data.get("course"),
    }
    students.append(new_student)

    return jsonify(new_student), 201


# PUT /students/<id> -> update a student's info
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    student["name"] = data.get("name", student["name"])
    student["age"] = data.get("age", student["age"])
    student["grade"] = data.get("grade", student["grade"])
    student["course"] = data.get("course", student["course"])

    return jsonify(student), 200


# DELETE /students/<id> -> remove a student
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students
    student = next((s for s in students if s["id"] == student_id), None)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message": "Student deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)
