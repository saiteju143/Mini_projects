from database import get_connection
connection=get_connection()
cursor=connection.cursor()

#students_table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email_id VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
""")

#courses_table
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

#enrollments_table
cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollments(
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_student
        FOREIGN KEY (student_id)
        REFERENCES students(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_course
        FOREIGN KEY (course_id)
        REFERENCES courses(id)
        ON DELETE CASCADE,
    CONSTRAINT unique_enrollment
        unique(student_id , course_id)
    );

""")

connection.commit()
cursor.close()
connection.close()

print("Tables created Successfully")


