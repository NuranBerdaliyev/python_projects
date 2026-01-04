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
        return f"General information about user {self.id}:\n" +\
        f"ID: {self.id}  |  Name: {self.name} | Email: {self.email} | Role: {self.role}"

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
    def __init__(self, name, email):
        super().__init__(name, email, 'Student')
        self.courses_id_list=[]  
        self.grades_d={}  
        

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
            elif grade<=0 or grade>5:
                raise ValueError("Wrong value for grade")
        else:
            raise TypeError("Wrong type for course")

    def get_average_grade(self):
        if len(self.grades_d.values())<=0:
            return None
        l=len(self.grades_d.values())
        avr=float(sum(self.grades_d.values())/l)
        return avr

class Teacher(User):
    def __init__(self, name, email):
        super().__init__(name, email, 'Teacher')
        self.courses_id_teaching_set=set()

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
                raise ValueError("There is either no student in this course, or no this course for teacher")
        else:
            raise TypeError("Wrong type for student or course or both")


class Course:
    course_count=1

    def __init__(self, title, max_students):
        self.id=Course.course_count
        if isinstance(title, str):
            self.title=title  
        else:
            raise TypeError("Wrong type for title")
        if isinstance(max_students, int):
            self.max_students=max_students  
        else:
            raise TypeError("Wrong type for max_students")
        self.teacher_id=None  
        self.students_id_list=[]
        Course.course_count+=1
        courses.append(self)

    
    def get_info(self):
        return f"General information about course:\n" +\
        f"ID: {self.id} | Title: {self.title}"+\
        f" | Real amount of students who enrolled {len(self.students_id_list)} |  Maximum amount of students: {self.max_students}" +\
        f" | Course's teacher: {self.teacher_id}"
    
    def __str__(self):
        return self.get_info()

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
    + "0. Exit\n1. Add teacher\n2. Add course\n3. Add student\n4. Assign student to course\n5. Assign teacher to course\n"\
        + "6. Drop student from course\n7. Grade student\n8. Id list of users(teachers, students)\n9. Id list of courses"))
    header="Id | Name | Email | Role"
    if i==1:
        name=input("Enter the name: ")
        email=input("Enter the email: ")
        t=Teacher(name, email)
        print("Teacher is added successfully!")
    elif i==2:
        title=input("Enter the title: ")
        max_students=int(input("How much students are there who can enroll the course? "))
        c=Course(title, max_students)
        print("Course is added successfully!")
    elif i==3:
        name=input("Enter the name: ")
        email=input("Enter the email: ")
        s=Student(name, email)
        print("Student is added successfully!")
    
    elif i==4:
        str1=""
        print(header)
        for u in users:
            if isinstance(u, Student):
                str1+=f"{str(u.id)} | {u.name} | {u.email} | {u.role}"
                str1+="\n"
        print(str1)
        student_id=int(input("Choose the student_id: "))
        str2=""
        print(header)
        for c in courses:
            if isinstance(c, Course):
                str2+=f"{c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                str2+="\n"
        print(str2)
        course_id=int(input("Choose the course_id: "))
        student=find_user_by_id(student_id)
        course=find_course_by_id(course_id)
        if isinstance(student, Student):
            student.enroll_course(course)
        print("Student was assigned to course successfully!")
    elif i==5:
        str1=""
        print(header)
        for u in users:
            if isinstance(u, Teacher):
                str1+=f"{str(u.id)} | {u.name} | {u.email} | {u.role}"
                str1+="\n"
        print(str1)
        teacher_id=int(input("Choose the teacher_id: "))
        str2=""
        print(header)
        for c in courses:
            if isinstance(c, Course):
                str2+=f"{c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                str2+="\n"
        print(str2)
        course_id=int(input("Choose the course_id: "))
        teacher=find_user_by_id(teacher_id)
        course=find_course_by_id(course_id)
        if isinstance(teacher, Teacher):
            teacher.assign_course(course)
        print("Teacher was assigned to course successfully!")
    elif i==6:
        str1=""
        print(header)
        for u in users:
            if isinstance(u, Student):
                str1+=f"{str(u.id)} | {u.name} | {u.email} | {u.role}"
                str1+="\n"
        print(str1)
        student_id=int(input("Choose the student_id: "))
        str2=""
        print(header)
        for c in courses:
            if isinstance(c, Course):
                str2+=f"{c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                str2+="\n"
        print(str2)
        course_id=int(input("Choose the course_id: "))
        student=find_user_by_id(student_id)
        course=find_course_by_id(course_id)
        if isinstance(student, Student):
            student.drop_course(course)
        print("Student was dropped from course successfully!")
    elif i==7:
        print(header)
        for c in courses:
            if isinstance(c, Course):
                str2+=f"{c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                str2+="\n"
        print(str2)
        course_id=int(input("Choose the course_id: "))
        course=find_course_by_id(course_id)

        str1=""
        print(header)
        for u in users:
            if isinstance(u, Student):
                str1+=f"{str(u.id)} | {u.name} | {u.email} | {u.role}"
                str1+="\n"
        print(str1)
        student_id=int(input("Choose the student_id: "))
        student=find_user_by_id(student_id)
        if isinstance(course, Course):
            if course.teacher_id==None:
                raise ValueError("You cannot assign grade from the course without teacher who was assigned")
            t=find_user_by_id(course.teacher_id)
            if isinstance(t, Teacher):
                grade=int(input("What is the grade you want to set? "))
                t.grade_student(student, course, grade)
            else:
                raise TypeError("Wrong type for teacher")
            print("The student got the grade successfully!")
        else:
            raise TypeError("Wrong type for course")
    elif i==0:
        print("Bye-Bye!")
        break


                    
