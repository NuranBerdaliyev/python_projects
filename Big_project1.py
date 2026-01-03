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
                course.add_student(self)
                self.courses_id_list.append(course.id)
                
        else:
            raise TypeError("Wrong type for course")
        
    def drop_course(self, course):
        if isinstance(course, Course):
            if course.id in self.courses_id_list:
                course.remove_student(self)
                self.courses_id_list.remove(course.id)
                
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
            self.teacher_id=teacher_id
        else:
            raise TypeError("Wrong type for teacher_id")
            
        
    def remove_student(self, student):
        if isinstance(student, Student):
            if student.id in self.students_id_list:
                self.students_id_list.remove(student.id)
            else:
                raise ValueError("Your student is already removed or he has not been in this course")
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
print("Welcome to my first local system!")
while True:
    i=int(input("You can choose one of these options by entering its point number:\n" \
          + "0. Exit\n1. Add teacher\n2. Add course\n3. Add student\n4. Assign student to course\n5. Assign teacher to course\n"))
    if i==1:
        name=input("Enter the name: ")
        email=input("Enter the email: ")
        course_teaching_id_set=set()
        t=Teacher(name, email, course_teaching_id_set)
        print("Teacher is added successfully!")
    elif i==2:
        title=input("Enter the title: ")
        max_students=int(input("How much students are there who can enroll the course? "))
        students_id_l=[]
        c=Course(title, max_students, students_id_l)
        print("Course is added successfully!")
    elif i==3:
        name=input("Enter the name: ")
        email=input("Enter the email: ")
        courses_id_list=[]
        grades_d={}
        s=Student(name, email, courses_id_list, grades_d)
        print("Student is added successfully!")
    elif i==4:
        str1=""
        for u in users:
            if isinstance(u, Student):
                str1+=f"Id | Name | Email | Role \n\
                    {str(u.id)} | {u.name} | {u.email} | {u.role}"
                str1+="\n"
        print(str1)
        student_id=int(input("Choose the student_id: "))
        str2=""
        for c in courses:
            if isinstance(c, Course):
                str2+=f"ID | Title | Max_students | Teacher_id \n\
                    {c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                str2+="\n"
        course_id=int(input("Choose the course_id: "))
        student=find_user_by_id(student_id)
        course=find_course_by_id(course_id)
        if isinstance(student, Student):
            student.enroll_course(course)
        print("Student was assigned to course successfully!")
    elif i==5:
        str1=""
        for u in users:
            if isinstance(u, Teacher):
                str1+=f"Id | Name | Email | Role \n\
                    {str(u.id)} | {u.name} | {u.email} | {u.role}"
                str1+="\n"
        print(str1)
        teacher_id=int(input("Choose the teacher_id: "))
        str2=""
        for c in courses:
            if isinstance(c, Course):
                str2+=f"ID | Title | Max_students | Teacher_id \n\
                    {c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                str2+="\n"
        course_id=int(input("Choose the course_id: "))
        teacher=find_user_by_id(teacher_id)
        course=find_course_by_id(course_id)
        if isinstance(teacher, Teacher):
            teacher.assign_course(course)
        print("Teacher was assigned to course successfully!")
    elif i==0:
        print("Bye-Bye!")
        break


                    
