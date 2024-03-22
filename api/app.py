from flask import Flask, request, jsonify
from models import db, Department, Job, Employee
from datetime import datetime
from utils import is_integer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@postgres/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")  ## Health check route
def check():
    return "<p>It's Ok!</p>"

@app.route('/upload', methods=['POST'])
def upload_csv():
    '''
        Route with function used to receive the posted csv files and evalutes by name
        and match with the right data model structure.

        Simple handling errors and checking of csv files pre uploading.
    '''
    db.create_all()
    uploaded_file = request.files.get('file')
    if not uploaded_file:
        return jsonify({'error': 'No file uploaded'}), 400
    filename = uploaded_file.filename
    data = []
    for line in uploaded_file.readlines():
        data.append(line.decode('utf-8').strip().split(','))
    print(data)
    for row in data:
        if filename.startswith('jobs'):
            new_entry = Job(
                id = row[0],
                job = row[1]
            )
        elif filename.startswith('departments'):
            new_entry = Department(
                id = row[0],
                department = row[1]
            )
        elif filename.startswith('hired_employees'):
            new_entry = Employee(
                id = row[0],
                name = row[1],
                datetime = row[2],
                department_id = is_integer(row[3]),
                job_id = is_integer(row[4]),
                partition_column = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            )
        else:
            return jsonify({'error': 'Invalid file name'}), 400

        db.session.add(new_entry)
    
    db.session.commit()

    return jsonify({'message': f'File "{filename}" uploaded successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True)
