import logging
logging.basicConfig(filename="e_learning.log", level=logging.INFO , format="%(asctime)s-%(levelname)s-%(message)s")


class User:

    def __init__(self,name,email,user_id):
        try:
            self.name=name
            self.email=email
            self.user_id=user_id
            logging.info("User created successfully")
        except Exception as e:
            print(f"Unexpected error while creating user:{e}")
            logging.error(f"Unexpected error while creating user:{e}")

    
class Course:

    def __init__(self,course_name):
        try:
            self.course_name=course_name
            self.progress={}
            
            logging.info("Course created successfully")
        except Exception as e:
            print(f"Error while creating course:{e}")

class Student(User):

    def __init__(self, name,email,user_id):
        try:
            super().__init__(name,email,user_id)
            self.enrolled_courses=[]
            logging.info(f"student {self.name} enrolled successfully")
        except Exception as e:
            print(f"Error while enrolling student {self.name}: ,{e} ")
            logging.error(f"Error while enrolling student {self.name}: ,{e} ")

    def enroll_course(self,course):
        try:
            if course in self.enrolled_courses:
                print(f"{self.name} ia already enrolled in {course.course_name}")
                logging.info(f"{self.name} ia already enrolled in {course.course_name}")
                return
            self.enrolled_courses.append(course)
            course.progress[self.user_id]=0
            print(f"{self.name} ia  enrolled in {course.course_name}")
            logging.info(f"{self.name} ia  enrolled in {course.course_name}")
        except Exception as e:
            print(f"Error while enrolling in course:{e}")
            logging.error(f"Error while enrolling in course:{e}")

    def view_enrolled_courses(self):
        try:
            if not self.enrolled_courses:
                print("Not enrolled any course")
                logging.info("Not enrolled any course")
                return
            for course in self.enrolled_courses:
                print(course.course_name)
            logging.info("Displayed enrolled courses")
            print("Displayed enrolled courses")

        except Exception as e:
            print(f"Unexpected error while viewing enrolled courses:{e}")
            logging.error("Unexpected error while viewing enrolled courses:{e}")

    def check_course_progress(self):
        try:
            if not self.enrolled_courses:
                print("Course enrolled is empty")
                return
            for course in self.enrolled_courses:
                progress=course.progress[self.user_id]
                print(f"{course.course_name} : {progress}%")
                logging.info(f"{course.course_name} : {progress}%")
        except Exception as e:
            print(f"error while checking progress:{e}")
            logging.error(f"error while checking progress:{e}")

class Instructor(User):

    def __init__(self,name,email,user_id):
        try:
            super().__init__(name,email,user_id)
            self.courses=[]
            logging.info(f"instructor {self.name} created successfully")
        except Exception as e:
            print(f"error while creating instructor {self.name}:{e}")
            logging.error(f"error while creating instructor {self.name}:{e}")

    def create_courses(self,course_name):
        try:
            course=Course(course_name)
            self.courses.append(course)
            print(f"{self.name} created course {course.course_name}")
            logging.info(f"{self.name} created course {course.course_name}")
            return course
        except Exception as e:
            print(f"Error while creating course: {e}")
            logging.error(f"Error while creating course: {e}")
            return None

    def display_courses(self):
            try:
                if not self.courses:
                    print("course list is empty")
                    return
                for course in self.courses:
                    print(course.course_name)
                print(f"Displayed courses successfully")
                logging.info(f"Displayed courses successfully")
                return course
            except Exception as e:
                print(f"Error while displaying course: {e}")
            logging.error(f"Error while diaplaying course: {e}")
            return None

instructor1 = Instructor(
    "Ravi",
    "ravi@gmail.com",
    "I101"
)

instructor2 = Instructor(
    "Priya",
    "priya@gmail.com",
    "I102"
)
student1 = Student(
    "Teju",
    "teju@gmail.com",
    "S101"
)

student2 = Student(
    "Anil",
    "anil@gmail.com",
    "S102"
)

course1 = instructor1.create_courses("Python")

course2 = instructor1.create_courses("SQL")

course3 = instructor2.create_courses("AWS")


student1.enroll_course(course1)
student1.enroll_course(course3)

student2.enroll_course(course2)
student2.enroll_course(course3)

student1.view_enrolled_courses()
student2.view_enrolled_courses()

student1.check_course_progress()
student2.check_course_progress()
        


    








