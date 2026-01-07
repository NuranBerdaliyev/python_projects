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
    try:
        i=int(input("You can choose one of these options by entering its point number:\n" \
        + "0. Exit\n1. Add teacher\n2. Add course\n3. Add student\n4. Assign student to course\n5. Assign teacher to course\n"\
        + "6. Drop student from course\n7. Grade student\n8. Id list of users(teachers, students)\n9. Id list of courses\n"\
        + "10. Look at the grades of student\n11. Look at course_list of teacher\n12. Look at course_list of student\n"))
    except ValueError or TypeError:
        print("Wrong type. Only string words")
        continue
    header="Id | Name | Email | Role"
    header2="Id | Title | Max_students | Teacher_id"
    if i==1:
        
        name=input("Enter the name: ")
        if name != name.strip():
            print("You have to enter name without whitespaces at the beginning and at the end")
            continue
        email=input("Enter the email: ")
        if not email.endswith("@kbtu.kz"):
            print("Must be ended with @kbtu.kz")
            continue
        t=Teacher(name, email)
        print("Teacher is added successfully!")
    elif i==2:
        title=input("Enter the title: ")
        if title!=title.strip():
            print("You have to enter title without whitespaces at the beginning and at the end")
        try:
            max_students=int(input("How much students are there who can enroll the course? "))
        except ValueError or TypeError:
            print("Wrong type. Title is string, max_students is integer")
            continue
        c=Course(title, max_students)
        print("Course is added successfully!")
    elif i==3:
        name=input("Enter the name: ")
        if name != name.strip():
            print("You have to enter name without whitespaces at the beginning and at the end")
            continue
        email=input("Enter the email: ")
        if not email.endswith("@kbtu.kz"):
            print("Must be ended with @kbtu.kz")
            continue
        s=Student(name, email)
        print("Student is added successfully!")
    
    elif i==4:
        str1=""
        print(header)
        for u in users:
            if isinstance(u, Student):
                str1=f"{str(u.id)} | {u.name} | {u.email} | {u.role}"
                print(str1)
        try:
            student_id=int(input("Choose the student_id: "))
        except ValueError or TypeError:
            print("Wrong type. Only integer")
            continue
        str2=""
        print(header2)
        for c in courses:
            if isinstance(c, Course):
                str2=f"{c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                print(str2)
        try:
            course_id=int(input("Choose the course_id: "))
        except ValueError or TypeError:
            print("Wrong type. Only integer")
            continue
        try:
            student=find_user_by_id(student_id)
            course=find_course_by_id(course_id)
            student.enroll_course(course)
        except AttributeError:
            print("Either student's or teacher's ID was not found in the main database")
            continue
        print("Student was assigned to course successfully!")
    elif i==5:
        str1=""
        print(header)
        for u in users:
            if isinstance(u, Teacher):
                str1=f"{str(u.id)} | {u.name} | {u.email} | {u.role}"
        print(str1)
        try:
            teacher_id=int(input("Choose the teacher_id: "))
        except ValueError or TypeError:
            print("Wrong type. Only integer")
            continue
        str2=""
        print(header2)
        for c in courses:
            if isinstance(c, Course):
                str2=f"{c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                
        print(str2)
        try:
            course_id=int(input("Choose the course_id: "))
        except ValueError or TypeError:
            print("Wrong type. Only integer")
            continue
        try:    
            teacher=find_user_by_id(teacher_id)
            course=find_course_by_id(course_id)
            teacher.assign_course(course)
        except AttributeError:
            print("Either student's or teacher's ID was not found in the main database")
            continue
        print("Teacher was assigned to course successfully!")
    elif i==6:
        str1=""
        print(header)
        for u in users:
            if isinstance(u, Student):
                str1=f"{str(u.id)} | {u.name} | {u.email} | {u.role}"
        print(str1)
        try:
            student_id=int(input("Choose the student_id: "))
        except ValueError or TypeError:
            print("Wrong type. Only integer")
            continue
        str2=""
        print(header2)
        for c in courses:
            if isinstance(c, Course):
                str2=f"{c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                
        print(str2)
        try:
            course_id=int(input("Choose the course_id: "))
        except ValueError or TypeError:
            print("Wrong type. Only integer")
            continue
        try:
            student=find_user_by_id(student_id)
            course=find_course_by_id(course_id)
            student.drop_course(course)
        except AttributeError:
            print("Either student's or teacher's ID was not found in the main database")
            continue
        print("Student was dropped from course successfully!")
    elif i==7:
        str2=""
        print(header2)
        for c in courses:
            if isinstance(c, Course):
                str2=f"{c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                
        print(str2)
        try:
            course_id=int(input("Choose the course_id: "))
        except ValueError or TypeError:
            print("Wrong type. Only integer")
            continue
        

        str1=""
        print(header)
        for u in users:
            if isinstance(u, Student):
                str1=f"{str(u.id)} | {u.name} | {u.email} | {u.role}"
        print(str1)
        try:
            student_id=int(input("Choose the student_id: "))
        except ValueError or TypeError:
            print("Wrong type. Only integer")
            continue
        try:
            course=find_course_by_id(course_id)
            student=find_user_by_id(student_id)
            if course.teacher_id==None:
                print("You cannot assign grade from the course without teacher who was assigned")
                continue
            try:
                grade=int(input("What is the grade you want to set? "))
            except TypeError:
                print("Wrong type. Only integer")
                continue
            t=find_user_by_id(course.teacher_id)
            t.grade_student(student, course, grade)
        except AttributeError:
            print("Either student's or teacher's ID was not found in the main database")
            continue
        print("The student got the grade successfully!")
        
    elif i==8:
        for u in users:
            print(u)
        print()
    elif i==9:
        for c in courses:
            print(c)
        print()
    elif i==10:
        try:
            s_id=int(input("Enter the student's id: "))
        except ValueError or TypeError:
            print("Wrong type. Only integer")
            continue
        try:
            s=find_user_by_id(s_id)
        

            for key, value in s.grades_d.items():
                print(f"Subject's ID: {key}; Grade: {value}\n")
            print(f"Average grade: {s.get_average_grade()}")
        except AttributeError:
            print("Either student's or teacher's ID was not found in the main database")
            continue
        except ValueError or TypeError:
            print("Not student")
            continue
    elif i==11:
        try:
            t_id = int(input("Enter the teacher_id: "))
        except ValueError or TypeError:
            print("Wrong type. Only integer")
            continue
        try:
            t=find_user_by_id(t_id)
            li=t.courses_id_teaching_set
            print("Course set which teacher teach:\n")
            for c_id in li:
                c=find_course_by_id(c_id)
                print(c)
        except AttributeError:
            print("Either student's or teacher's ID was not found in the main database")
            continue

    elif i==12: 
        try:
            s_id=int(input("Enter the student_id: "))
        except ValueError or TypeError:
            print("Wrong type. Only integer")
            continue
        try:
            s=find_user_by_id(s_id)
            li=s.courses_id_list
            print("Course list which student study in: \n")
            for c_id in li:
                c=find_course_by_id(c_id)
                print(c)
        except AttributeError:
            print("Either student's or teacher's ID was not found in the main database")
            continue
    elif i==0:
        print("Bye-Bye!")
        break