

class User:
    users=[]
    user_count = 1
    allowed_roles = {'Teacher', 'Student'}
    def __init__(self, name, email, role):
        self.id=User.user_count
        if isinstance(name, str):
            self.name=name
        else:
            raise WrongNameType("Wrong type for name") 
        self.validate_email(email)
        self.email=email
            
        if isinstance(role, str):
            if role in User.allowed_roles:
                self.role=role  
            else:
                raise WrongRoleValue("Role is neither Teacher nor Student")
        else:
            raise WrongRoleType("Wrong type for role")
        User.user_count+=1
        User.users.append(self)
    def get_info(self):
        return f"General information about user {self.id}:\n" +\
        f"ID: {self.id}  |  Name: {self.name} | Email: {self.email} | Role: {self.role}"

    def __str__(self):
        return self.get_info()

    @staticmethod
    def validate_email(email):
        if not isinstance(email, str):
            raise WrongEmailType("Wrong type for email")
        if not email.endswith('@kbtu.kz'):
            raise WrongDomainEnd("Not ended with @kbtu.kz")
        else:
            return True
    @staticmethod
    def find_user_by_id(user_id):
        for user in User.users:
            if user.id == user_id:
                return user
        return None
    
class WrongDomainEnd(ValueError):
    pass
class WrongRoleValue(ValueError):
    pass
class WrongEmailType(TypeError):
    pass
class WrongNameType(TypeError):
    pass
class WrongRoleType(TypeError):
    pass
        
    
class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email, 'Student')
        self.courses_id_set=set() 
        self.grades_d={}  
        

    def enroll_course(self, course):
        if isinstance(course, Course):
            course.add_student(self)
            self.courses_id_set.add(course.id)
            self.grades_d[course.id]=None
                
        else:
            raise WrongCourseType("Wrong type for course")
        
    def drop_course(self, course):
        if isinstance(course, Course):
            course.remove_student(self)
            self.courses_id_set.discard(course.id)
            self.grades_d.pop(course.id)
                
        else:
            raise WrongCourseType("Wrong type for course")
    
    def set_grade(self, course, grade):
        if isinstance(course, Course):
            if course.id in self.courses_id_set and 0<grade<=5:
                self.grades_d[course.id]=grade
            else:
                raise WrongGradeValue("Wrong value for grade")
        else:
            raise WrongCourseType("Wrong type for course")


    def get_average_grade(self):
        if len(self.grades_d.values())<=0:
            return None
        grades=[g for g in self.grades_d.values() if g is not None]
        l=len(grades)
        avr=float(sum(grades)/l)
        return avr

class WrongCourseType(TypeError):
    pass
class WrongGradeValue(ValueError):
    pass

class Teacher(User):
    def __init__(self, name, email):
        super().__init__(name, email, 'Teacher')
        self.courses_id_teaching_set=set()

    def assign_course(self, course):
        if isinstance(course, Course):
            course.assign_teacher(self.id)
            self.courses_id_teaching_set.add(course.id)
        else:
            raise WrongCourseType("Wrong type for course")

    def grade_student(self, student, course, grade):
        if isinstance(student, Student) and isinstance(course, Course):
            if course.id in self.courses_id_teaching_set and course.id in student.courses_id_set:
                student.set_grade(course, grade)
            else:
                raise NotFoundCourseForTeacher("There is either no student in this course, or no this course for teacher")
        else:
            raise WrongStudent_CourseType("Wrong type for student or course or both")

class NotFoundCourseForTeacher(ValueError):
    pass
class WrongStudent_CourseType(TypeError):
    pass

class Course:
    courses=[]
    course_count=1

    def __init__(self, title, max_students):
        self.id=Course.course_count
        if isinstance(title, str):
            self.title=title  
        else:
            raise WrongTitleType("Wrong type for title")
        if isinstance(max_students, int):
            self.max_students=max_students  
        else:
            raise WrongMaxStudentsType("Wrong type for max_students")
        self.teacher_id=None  
        self.students_id_set=set()
        Course.course_count+=1
        Course.courses.append(self)

    
    def get_info(self):
        return f"General information about course:\n" +\
        f"ID: {self.id} | Title: {self.title}"+\
        f" | Real amount of students who enrolled {len(self.students_id_set)} |  Maximum amount of students: {self.max_students}" +\
        f" | Course's teacher: {self.teacher_id}"
    
    def __str__(self):
        return self.get_info()

    def add_student(self, student):
        if isinstance(student, Student):
            if student.id not in self.students_id_set and not self.is_full():
                self.students_id_set.add(student.id)
            elif self.is_full():
                raise CourseIsFull("Course is full")
        else:
            raise WrongStudentType("Wrong type of student")

    def assign_teacher(self, teacher_id):
        if isinstance(teacher_id, int):
            self.teacher_id=teacher_id
        else:
            raise WrongTeacherIDType("Wrong type for teacher_id")
            
        
    def remove_student(self, student):
        if isinstance(student, Student):
            if student.id in self.students_id_set:
                self.students_id_set.remove(student.id)
            else:
                raise StudentIsNotEnrolled("This student is not enrolled in this course")
        else:
            raise WrongStudentType("Wrong type of student")

    def is_full(self):
        return len(self.students_id_set)>=self.max_students
    @staticmethod
    def find_course_by_id(course_id):
        for course in Course.courses:
            if course.id == course_id:
                return course
        return None

class WrongTitleType(TypeError):
    pass
class WrongMaxStudentsType(TypeError):
    pass
class CourseIsFull(ValueError):
    pass
class WrongStudentType(TypeError):
    pass
class WrongTeacherIDType(TypeError):
    pass
class StudentIsNotEnrolled(ValueError):
    pass



def main():
    print("Welcome to my first local system!")
    while True:
        try:
            i=int(input("You can choose one of these options by entering its point number:\n" \
            + "0. Exit\n1. Add teacher\n2. Add course\n3. Add student\n4. Assign student to course\n5. Assign teacher to course\n"\
            + "6. Drop student from course\n7. Grade student\n8. Id list of users(teachers, students)\n9. Id list of courses\n"\
            + "10. Look at the grades of student\n11. Look at course_list of teacher\n12. Look at course_list of student\n"))
        except (ValueError, TypeError):
            print("Wrong type. Only string words")
            continue
        
        header="Id | Name | Email | Role"
        header2="Id | Title | Max_students | Teacher_id"
        if i==1:
            name=input("Enter the name: ").strip()
            email=input("Enter the email: ").strip()
            if not (name and email):
                print("Must not be empty")
                continue
            try:
                t=Teacher(name, email)
                print("Teacher is added successfully!")
            except WrongDomainEnd as wde:
                print(wde)
                continue
        elif i==2:
            title=input("Enter the title: ").strip()
            if not title:
                print("Must not be empty")
                continue
            try:
                max_students=int(input("How much students are there who can enroll the course? ").strip())
            except (ValueError, TypeError):
                print("Wrong type. Max_students is integer")
                continue
            c=Course(title, max_students)
            print("Course is added successfully!")
        elif i==3:
            name=input("Enter the name: ").strip()
            email=input("Enter the email: ").strip()
            if not(name and email):
                print("Must not be empty")
                continue
            try:
                s=Student(name, email)
                print("Student is added successfully!")
            except WrongEmailType as wet:
                print(wet)
                continue
        
        elif i==4:
            str1=""
            print(header)
            for u in User.users:
                if isinstance(u, Student):
                    str1=f"{str(u.id)} | {u.name} | {u.email} | {u.role}"
                    print(str1)
            try:
                student_id=int(input("Choose the student_id: "))
            except (ValueError, TypeError):
                print("Wrong type. Only integer")
                continue
            str2=""
            print(header2)
            for c in Course.courses:
                if isinstance(c, Course):
                    str2=f"{c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                    print(str2)
            try:
                course_id=int(input("Choose the course_id: "))
            except (ValueError, TypeError):
                print("Wrong type. Only integer")
                continue
            
            student=User.find_user_by_id(student_id)
            course=Course.find_course_by_id(course_id)
            if not isinstance(student, Student):
                print("Student was not found")
                continue
            if not isinstance(course, Course):
                print("Course was not found")
                continue
            try:
                student.enroll_course(course)
            except CourseIsFull as cif:
                print(cif)
                continue
            
            
            print("Student was assigned to course successfully!")
        elif i==5:
            str1=""
            print(header)
            for u in User.users:
                if isinstance(u, Teacher):
                    str1=f"{str(u.id)} | {u.name} | {u.email} | {u.role}"
                    print(str1)
            try:
                teacher_id=int(input("Choose the teacher_id: "))
            except (ValueError, TypeError):
                print("Wrong type. Only integer")
                continue
            str2=""
            print(header2)
            for c in Course.courses:
                if isinstance(c, Course):
                    str2=f"{c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                    print(str2)
            try:
                course_id=int(input("Choose the course_id: "))
            except (ValueError, TypeError):
                print("Wrong type. Only integer")
                continue  
            teacher=User.find_user_by_id(teacher_id)
            course=Course.find_course_by_id(course_id)
            if not isinstance(teacher, Teacher):
                print("Teacher was not found")
                continue
            if not isinstance(course, Course):
                print("Course was not found")
                continue
            teacher.assign_course(course)
            print("Teacher was assigned to course successfully!")
        elif i==6:
            str1=""
            print(header)
            for u in User.users:
                if isinstance(u, Student):
                    str1=f"{u.id} | {u.name} | {u.email} | {u.role}"
                    print(str1)
            try:
                student_id=int(input("Choose the student_id: "))
            except (ValueError, TypeError):
                print("Wrong type. Only integer")
                continue
            str2=""
            print(header2)
            for c in Course.courses:
                if isinstance(c, Course):
                    str2=f"{c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                    print(str2)
            try:
                course_id=int(input("Choose the course_id: "))
            except (ValueError, TypeError):
                print("Wrong type. Only integer")
                continue
            student=User.find_user_by_id(student_id)
            course=Course.find_course_by_id(course_id)
            if not isinstance(student, Student):
                print("Student was not found")
                continue
            if not isinstance(course, Course):
                print("Course was not found")
                continue
            try:
                student.drop_course(course)
            except StudentIsNotEnrolled as sine:
                print(sine)
                continue
            
            print("Student was dropped from course successfully!")
        elif i==7:
            str2=""
            print(header2)
            for c in Course.courses:
                if isinstance(c, Course):
                    str2=f"{c.id} | {c.title} | {c.max_students} | {c.teacher_id}"
                    print(str2)
            try:
                course_id=int(input("Choose the course_id: "))
            except (ValueError, TypeError):
                print("Wrong type. Only integer")
                continue
            

            str1=""
            print(header)
            for u in User.users:
                if isinstance(u, Student):
                    str1=f"{str(u.id)} | {u.name} | {u.email} | {u.role}"
                    print(str1)
            try:
                student_id=int(input("Choose the student_id: "))
            except (ValueError, TypeError):
                print("Wrong type. Only integer")
                continue
            
            course=Course.find_course_by_id(course_id)
            student=User.find_user_by_id(student_id)
            if not isinstance(student, Student):
                print("Student was not found")
                continue
            if not isinstance(course, Course):
                print("Course was not found")
                continue
            if course.teacher_id==None:
                print("You cannot assign grade from the course without teacher who was assigned")
                continue
            try:
                grade=int(input("What is the grade you want to set? "))
            except (ValueError, TypeError):
                print("Wrong type. Only integer. Grade has to be between ")
                continue
            t=User.find_user_by_id(course.teacher_id)
            if not isinstance(t, Teacher):
                print("Teacher of this course is not teacher")
                continue
            try:
                t.grade_student(student, course, grade)
            except WrongGradeValue as wgv:
                print(wgv)
                continue
            except NotFoundCourseForTeacher as nfcft:
                print(nfcft)
                continue
            
        elif i==8:
            for u in User.users:
                print(u)
            print()
        elif i==9:
            for c in Course.courses:
                print(c)
            print()
        elif i==10:
            try:
                s_id=int(input("Enter the student's id: "))
            except (ValueError, TypeError):
                print("Wrong type. Only integer")
                continue
            
            s=User.find_user_by_id(s_id)
            if not isinstance(s, Student):
                print("ID doesn't belong to student")
                continue
            for key, value in s.grades_d.items():
                print(f"Subject's ID: {key}; Grade: {value}")
            print(f"Average grade: {s.get_average_grade()}")
        elif i==11:
            try:
                t_id = int(input("Enter the teacher_id: "))
            except (ValueError, TypeError):
                print("Wrong type. Only integer")
                continue
            t=User.find_user_by_id(t_id)
            if not isinstance(t, Teacher):
                print("ID doesn't belong to teacher")
                continue
            li=t.courses_id_teaching_set
            print("Course set which teacher teach:\n")
            for c_id in li:
                c=Course.find_course_by_id(c_id)
                print(c)

        elif i==12: 
            try:
                s_id=int(input("Enter the student_id: "))
            except (ValueError, TypeError):
                print("Wrong type. Only integer")
                continue
            s=User.find_user_by_id(s_id)
            if not isinstance(s, Student):
                print("ID doesn't belong to student")
                continue
            li=s.courses_id_set
            print("Course set which student study in: \n")
            for c_id in li:
                c=Course.find_course_by_id(c_id)
                print(c)
        elif i==0:
            print("Bye-Bye!")
            break

if __name__=="__main__":
    main()