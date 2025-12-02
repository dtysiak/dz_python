from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String)

class StudentCourse(Base):
    __tablename__ = "student_course"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))

engine = create_engine("sqlite:///simple_students.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_courses():
    titles = ["С#", "Python", "QA", "SQL"]
    for t in titles:
        session.add(Course(title=t))
    session.commit()

def create_students():
    for i in range(1, 21):
        session.add(Student(name=f"Student {i}"))
    session.commit()

def register_students(student_id, course_id):
    sc = StudentCourse(student_id=student_id, course_id=course_id)
    session.add(sc)
    session.commit()

def add_new_student(name, course_id):
    student = Student(name=name)
    session.add(student)
    session.commit()

    register_students(student.id, course_id)

def show_students(course_id):
    students = session.query(StudentCourse).filter_by(course_id=course_id).all()
    result = []
    for item in students:
        st = session.query(Student).get(item.student_id)
        result.append(st.name)
    return result

def show_courses_of_student(student_id):
    links = session.query(StudentCourse).filter_by(student_id=student_id).all()
    result = []
    for item in links:
        course = session.query(Course).get(item.course_id)
        result.append(course.title)
    return result

def update_student(student_id, new_name):
    st = session.query(Student).get(student_id)
    st.name = new_name
    session.commit()

def delete_student(student_id):
    st = session.query(Student).get(student_id)
    session.delete(st)
    session.commit()

if __name__ == "__main__":
    create_courses()
    create_students()

    add_new_student("Diana", 1)

    print("Courses of Student:", show_courses_of_student(1))
    print("Students on the course:", show_students(1))

    update_student(1, "New Name")
    delete_student(20)
