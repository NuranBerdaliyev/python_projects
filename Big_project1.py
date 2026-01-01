users=[]
courses=[]
class User:
    user_count = 1
    allowed_roles = {'Teacher', 'Student'}
    def __init__(self, name, email, role):
        self.id=User.user_count
        if isinstance(name, str):
            self.name=name
        else:
            raise TypeError("Wrong type for name") 
        self.validate_email(email)
        self.email=email
            
        if isinstance(role, str):
            if role in User.allowed_roles:
                self.role=role  
            else:
                raise ValueError("Role is neither Teacher nor Student")
        else:
            raise TypeError("Wrong type for role")
        User.user_count+=1
        users.append(self)
    def get_info(self):
        return f"General information about user {self.id}:\n \
            ID: {self.id}  |  Name: {self.name} | Email: {self.email} | Role: {self.role}"

    def __str__(self):
        return self.get_info()

    @staticmethod
    def validate_email(email):
        if not isinstance(email, str):
            raise TypeError("Wrong type for email")
        if not email.endswith('@kbtu.kz'):
            raise ValueError("Not ended with @kbtu.kz")
        else:
            return True
        
    
class Student(User):
    def __init__(self, name, email, courses_id_list, grades_d):
        super().__init__(name, email, 'Student')
        if isinstance(courses_id_list, list):
            self.courses_id_list=courses_id_list  
        else:
            raise TypeError("Wrong type for courses_id_list")
        if isinstance(grades_d, dict):
            self.grades_d=grades_d  
        else:
            raise TypeError("Wrong type for grades_d")

    def enroll_course(self, course):
        if isinstance(course, Course):
            if course.id not in self.courses_id_list:
                self.courses_id_list.append(course.id)
                course.add_student(self)
        else:
            raise TypeError("Wrong type for course")
        
    def drop_course(self, course):
        if isinstance(course, Course):
            if course.id in self.courses_id_list:
                self.courses_id_list.remove(course.id)
                course.remove_student(self)
        else:
            raise TypeError("Wrong type for course")
    
    def set_grade(self, course, grade):
        if isinstance(course, Course):
            if course.id in self.courses_id_list and 0<grade<=5:
                self.grades_d[course.id]=grade
        else:
            raise TypeError("Wrong type for course")

    def get_average_grade(self):
        if len(self.grades_d.values())<=0:
            return None
        l=len(self.grades_d.values())
        avr=float(sum(self.grades_d.values())/l)
        return avr

class Teacher(User):
    def __init__(self, name, email, courses_id_teaching_set):
        super().__init__(name, email, 'Teacher')
        if isinstance(courses_id_teaching_set, set):
            self.courses_id_teaching_set=courses_id_teaching_set  
        else:
            raise TypeError("Wrong type of courses_id_teaching_set")

    def assign_course(self, course):
        if isinstance(course, Course):
            course.assign_teacher(self.id)
            self.courses_id_teaching_set.add(course.id)
        else:
            raise TypeError("Wrong type for course")

    def grade_student(self, student, course, grade):
        if isinstance(student, Student) and isinstance(course, Course):
            if course.id in self.courses_id_teaching_set and course.id in student.courses_id_list:
                student.set_grade(course, grade)
        else:
            raise TypeError("Wrong type for student or course or both")


class Course:
    course_count=1

    def __init__(self, title, max_students, students_id_l, teacher_id=None):
        self.id=Course.course_count
        if isinstance(title, str):
            self.title=title  
        else:
            raise TypeError("Wrong type for title")
        if isinstance(max_students, int):
            self.max_students=max_students  
        else:
            raise TypeError("Wrong type for max_students")
        if isinstance(students_id_l, list):
            if len(students_id_l)<=max_students and len(students_id_l)>=0:
                self.students_id_list=students_id_l   
            else: raise ValueError("Not correct length")
        else:
            raise TypeError("Wrong type for students_id_l")
        if isinstance(teacher_id, int) or teacher_id==None:
            self.teacher_id=teacher_id  
        else:
            raise TypeError("Wrong Type for teacher_id")
        Course.course_count+=1
        courses.append(self)


    def add_student(self, student):
        if isinstance(student, Student):
            if student.id not in self.students_id_list and not self.is_full():
                self.students_id_list.append(student.id)
            else:
                raise ValueError("Your student already exists or there is no place for him")
        else:
            raise TypeError("Wrong type of student")

    def assign_teacher(self, teacher_id):
        if isinstance(teacher_id, int):
            if teacher_id!=None:
                self.teacher_id=teacher_id
        else:
            raise TypeError("Wrong type for teacher_id")
            
        
    def remove_student(self, student):
        if isinstance(student, Student):
            if student.id in self.students_id_list:
                self.students_id_list.remove(student.id)
            else:
                return "Your student is already removed or he has not been in this course"
        else:
            raise TypeError("Wrong type of student")

    def is_full(self):
        return len(self.students_id_list)>=self.max_students

def find_user_by_id(user_id):
    for user in users:
        if user.id == user_id:
            return user
    return None
def find_course_by_id(course_id):
    for course in courses:
        if course.id == course_id:
            return course
    return None
    
    
print("s")