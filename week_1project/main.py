from flask import Flask, request, jsonify, abort

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 20,
        "gender": "male",
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "age": 21,
        "gender": "female",
    },
    {
        "id": 3,
        "name": "Jim Doe",
        "email": "jim.doe@example.com",
        "age": 22,
        "gender": "male",
    },
    {
        "id": 4,
        "name": "Jill Doe",
        "email": "jill.doe@example.com",
        "age": 23,
        "gender": "female",
    },
    {
        "id": 5,
        "name": "Jack Doe",
        "email": "jack.doe@example.com",
        "age": 24,
        "gender": "male",
    }
]

next_student_id = len(students) + 1


@app.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve a list of all students with pagination support.
    """
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    start = (page - 1) * limit
    end = start + limit
    paginated_students = students[start:end]
    
    return jsonify({
        "students": paginated_students,
        "page": page,
        "limit": limit
    })

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Retrieve a single student by ID.
    """
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        abort(404)
    return jsonify(student)

@app.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student record.
    """
    global next_student_id
    if not request.json or 'name' not in request.json:
        abort(400, description="Name field is required.")
        
    new_student = {
        "id": next_student_id,
        "name": request.json['name'],
        "email": request.json.get('email', ""),
        "age": request.json.get('age', 0),
        "gender": request.json.get('gender', ""),
    }
    students.append(new_student)
    next_student_id += 1
    return jsonify(new_student), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """
    Update an existing student record by ID.
    """
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        abort(404)

    if not request.json:
        abort(400)

    student.update({
        'name': request.json.get('name', student['name']),
        'email': request.json.get('email', student['email']),
        'age': request.json.get('age', student['age']),
        'gender': request.json.get('gender', student['gender']),
    })
    return jsonify(student)

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """
    Delete a student record by ID.
    """
    global students
    student_to_delete = next((s for s in students if s['id'] == student_id), None)
    if student_to_delete is None:
        abort(404)

    students = [s for s in students if s['id'] != student_id]
    return jsonify(student_to_delete)

@app.errorhandler(404)
def not_found(error):
    """Global 404 error handler."""
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(Exception)
def handle_exception(error):
    """Global exception handler."""

    return jsonify({
        "error": "An error occurred", 
        "message": str(error)
    }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)