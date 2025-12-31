import copy
import json
import time

class Course:
    id:int=0
    name:str=""
    units:int=0
    score:float=0.0
    def __init__(self,id,name,units):
        self.id=id
        self.name=name
        self.units=units
        self.score=0.0
    def __eq__ (self,other):
        return self.id==other.id
    def __str__ (self):
        return f"{self.id}\t{self.name}\t{self.units}"

class Student:
    id:int=0
    name:str=""
    family:str=""
    courses:list[Course]=[]
    def __init__(self,id,name,family):
        self.id=id
        self.name=name
        self.family=family
        self.courses=[]
    def __eq__ (self,other):
        return self.id==other.id
    def __str__ (self):
        return f"{self.id}\t{self.name}\t{self.family}"
    
class Teacher:
    id:int=0
    name:str=""
    family:str=""
    grade:str=""
    courses:list[Course]=[]
    def __init__(self,id,name,family,grade):
        self.id=id
        self.name=name
        self.family=family
        self.grade=grade
        self.courses=[]
    def __eq__ (self,other):
        return self.id==other.id
    def __str__ (self):
        return f"{self.id}\t{self.name}\t{self.family}\t{self.grade}"

class Classroom:
    id:int=0
    name:str=""
    course:Course=None
    teacher:Teacher=None
    students:list[Student]=[]
    def __init__(self,id,name,course,teacher,students):
        self.id=id
        self.name=name
        self.course=course
        self.teacher=teacher
        self.students=students
    def __str__ (self):
        return f"{self.id}\t{self.name}"
    def __eq__ (self,other):
        return self.id==other.id

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number")

students=[]
teachers=[]
courses=[]
classrooms=[]
selected_student_index=-1
selected_teacher_index=-1
selected_classroom_index=-1
exit_check=False


with open("data.json","rt") as f1:
    d1=f1.read()
    data=json.loads(d1)

for course in data["Courses"]:
    id=course["id"]
    name=course["name"]
    units=course["units"]
    c1=Course(id,name,units)
    courses.append(c1)

for student in data["Students"]:
    id=student["id"]
    name=student["name"]
    family=student["family"]
    s1=Student(id,name,family)
    for crs,score in student["courses"]:
        c1=Course(crs,"",0)
        if c1 in courses:
            ind=courses.index(c1)
            c2=copy.deepcopy(courses[ind])
            c2.score=score
            s1.courses.append(c2)
    students.append(s1)

for teacher in data["Teachers"]:
    id=teacher["id"]
    name=teacher["name"]
    family=teacher["family"]
    grade=teacher["grade"]
    t1=Teacher(id,name,family,grade)
    for crs in teacher["courses"]:
        c1=Course(crs,"",0)
        if c1 in courses:
            ind=courses.index(c1)
            c2=courses[ind]
            t1.courses.append(c2)
    teachers.append(t1)

for classroom in data["Classrooms"]:
    id=classroom["id"]
    name=classroom["name"]
    id_course=classroom["course"]
    c1=Course(id_course,"","")
    if c1 in courses:
        course=courses[courses.index(c1)]
    id_teacher=classroom["teacher"]
    t1=Teacher(id_teacher,"","","")
    if t1 in teachers:
        teacher=teachers[teachers.index(t1)]
    students_classroom=[]
    for id_student in classroom["students"]:
        s1=Student(id_student,"","")
        if s1 in students:
            students_classroom.append(students[students.index(s1)])
    c2=Classroom(id,name,course,teacher,students_classroom)  
    classrooms.append(c2)
    
level="root"
while True:
    if level=="root":
        menus=["1.students","2.teachers","3.courses","4.classrooms","5.save","0.exit"]
        for menu in menus :
            time.sleep(0.1)
            print(menu)
        cmd= get_int(">>")
        if cmd==1:
            level="students"
        elif cmd==2:
            level="teachers"
        elif cmd==3:
            level="courses"       
        elif cmd==4:
            level="classrooms"        
        elif cmd ==5 :
            level="save"
        elif cmd==0:
            level="exit"


    elif level=="students":
        menus=["1.add student","2.edit student","3.delete student","4.view students","5.select student","0.back"]
        for menu in menus :
            time.sleep(0.1)
            print(menu)
        cmd= get_int(">>")
        if cmd==1:
            id=get_int("id: ")
            name=str(input("name: "))
            family=str(input("family: "))
            s1=Student(id,name,family)
            if s1 in students:
                print("alredy exits")
            else:
                students.append(s1)
        elif cmd==2:
            for student in students:
                print(student)
            id=get_int("id: ")
            s1=Student(id,"","")
            if s1 in students:
                students.remove(s1)
                name=str(input("name: "))
                family=str(input("family: "))
                s1=Student(id,name,family)
                students.append(s1)
            else:
                print("doesnt exits")
        elif cmd==3:
            for student in students:
                print(student)
            id=get_int("id: ")
            s1=Student(id,"","")
            if s1 in students:
                check_classroom=[False if s1 in classroom.students else True for classroom in classrooms]
                if all(check_classroom):
                    students.remove(s1)
                else:
                    print("cannot delete")
            else:
                print("doesnt exits")
        elif cmd==4:
            for student in students:
                print(student)
        elif cmd==5:
            for student in students:
                print(student)
            id=get_int("id: ")
            s1=Student(id,"","")
            if s1 in students:
                selected_student_index=students.index(s1)
                level="student_select"
            else:
                print("doesnt exits")
        elif cmd==0:
            level="root"

    elif level=="teachers":
        menus=["1.add teacher","2.edit teacher","3.delete teacher","4.view teachers","5.select teacher","0.back"]
        for menu in menus :
            time.sleep(0.1)
            print(menu)
        cmd= get_int(">>")
        if cmd==1: 
            id=get_int("id: ")
            name=str(input("name: "))
            family=str(input("family: "))
            grade=str(input("grade: "))
            s1=Teacher(id,name,family,grade)
            if s1 in teachers:
                print("alredy exits")
            else:
                teachers.append(s1)
        elif cmd==2:
            for teacher in teachers:
                print(teacher)
            id=get_int("id: ")
            t1=Teacher(id,"","","")
            if t1 in teachers:
                teachers.remove(t1)
                name=str(input("name: "))
                family=str(input("family: "))
                grade=str(input("grade: "))
                s1=Teacher(id,name,family,grade)
                teachers.append(t1)
            else:
                print("doesnt exits")
        elif cmd==3:
            for teacher in teachers:
                print(teacher)
            id=get_int("id: ")
            t1=Teacher(id,"","","")
            if t1 in teachers:
                print(teachers[teachers.index(t1)])
                check_classroom=[False if t1.id == classroom.teacher.id else True for classroom in classrooms]
                if all(check_classroom):
                    teachers.remove(t1)
                else:
                    print("cannot delete")
            else:
                print("doesnt exits")
        elif cmd==4:
            for teacher in teachers:
                print(teacher)
        elif cmd==5:
            for teacher in teachers:
                print(teacher)
            id=get_int("id: ")
            t1=Teacher(id,"","","")
            if t1 in teachers:
                selected_teacher_index=teachers.index(t1)
                level="teacher_select"
            else:
                print("doesnt exits")
        elif cmd==0:
            level="root"
        
    elif level=="courses":
        menus=["1.add course","2.edit course","3.delete course","4.view courses","0.back"]
        for menu in menus :
            time.sleep(0.1)
            print(menu)
        cmd= get_int(">>")
        if cmd==1:
            id=get_int("id: ")
            name=str(input("name: "))
            units=get_int("units: ")
            c1=Course(id,name,units)
            print(c1)
            if c1 in courses:
                print("alredy exits")
            else:
                courses.append(c1)
        elif cmd==2:
            for course in courses:
                print(course)
            id=get_int("id: ")
            c1=Course(id,"","")
            if c1 in courses:
                courses.remove(c1)
                name=str(input("name: "))
                units=get_int("units: ")
                c1=Course(id,name,units)
                courses.append(c1)
            else:
                print("doesnt exits")
        elif cmd==3:
            for course in courses:
                print(course)
            id=get_int("id: ")
            c1=Course(id,"","")
            if c1 in courses:
                check_student=[False if c1 in student.courses else True for student in students ]
                if all(check_student):
                    check_teacher=[False if c1 in teacher.courses else True for teacher in teachers ]
                    if all(check_teacher):
                        check_classroom=[False if c1.id == classroom.course.id else True for classroom in classrooms ]
                        if all(check_classroom):
                            courses.remove(c1)
                        else:
                            print("cannot delete")
                    else:
                        print("cannot delete")
                else:
                    print("cannot delete")
            else:
                print("does not exit")
        elif cmd==4:
            for course in courses:
                print(course)
        elif cmd==0:
            level="root"

    elif level=="classrooms":
        menus=["1.add classroom","2.edit classroom","3.delete classroom","4.view classrooms","5.select classroom","0.back"]
        for menu in menus :
            time.sleep(0.1)
            print(menu)
        cmd= get_int(">>")
        if cmd==1:
            id=get_int("id: ")
            name=str(input("name: "))
            for course in courses:
                print(course)
            id_course=get_int("id course: ")
            c1=Course(id_course,"","")
            if c1 in courses:
                course=courses[courses.index(c1)]
            else:
                print("does not exist")

            for teacher in teachers:
                if c1 in teacher.courses:
                    print(teacher)
            id_teacher=get_int("id teacher: ")
            t1=Teacher(id_teacher,"","","")
            if t1 in teachers:
                teacher=teachers[teachers.index(t1)]
            else:
                print("does not exist")

            for student in students:
                if c1 in student.courses and student.courses[student.courses.index(c1)].score<10:
                    print(student)
            students_classroom=[]
            while True:
                id_student=get_int("id student: ")
                s1=Student(id_student,"","")
                if id_student==0:
                    break
                elif s1 in students:
                    students_classroom.append(students[students.index(s1)])
                else:
                    print("not found")

            c1=Classroom(id,name,course,teacher,students_classroom)  
            classrooms.append(c1)
            
        elif cmd==2:
            for classroom in classrooms:
                print(classroom)
            id=get_int("id: ")
            c1=Classroom(id,"","","",[])
            if c1 in classrooms:
                name=str(input("new name: "))
                classrooms[classrooms.index(c1)].name=name
            else:
                print("not found")
        elif cmd==3:
            for classroom in classrooms:
                print(classroom)
            id=get_int("id: ")
            c1=Classroom(id,"","","",[])
            if c1 in classrooms:    
                classrooms.remove(c1)
            else:
                print("not found")
        elif cmd==4:
            for c1 in classrooms:
                print(f"\nClassroom:\n{c1}\ncourse:\t{c1.course}")
        elif cmd==5:
            for classroom in classrooms:
                print(classroom)
            id=get_int("id: ")
            c1=Classroom(id,"","","",[])  
            if c1 in classrooms:
                level="select_classroom"
                selected_classroom_index=classrooms.index(c1)

        elif cmd==0:
            level="root"

    elif level=="save":
        data={}
        s1=[]
        for student in students:
            s2={}
            s2["id"]=student.id
            s2["name"]=student.name
            s2["family"]=student.family
            c1=[]
            for course in student.courses:
                c2=[]
                c2.append(course.id)
                c2.append(course.score)
                c1.append(c2)
            s2["courses"]=c1
            s1.append(s2)
        data["Students"]=s1

        t1=[]
        for teacher in teachers:
            t2={}
            t2["id"]=teacher.id
            t2["name"]=teacher.name
            t2["family"]=teacher.family
            t2["grade"]=teacher.grade
            c1=[]
            for course in teacher.courses:
                c1.append(course.id)
            t2["courses"]=c1
            t1.append(t2)
        data["Teachers"]=t1

        c1=[]
        for course in courses:
            c2={}
            c2["id"]=course.id
            c2["name"]=course.name
            c2["units"]=course.units
            c1.append(c2)
        data["Courses"]=c1

        c1=[]
        for classroom in classrooms:
            c2={}
            c2["id"]=classroom.id
            c2["name"]=classroom.name
            c2["teacher"]=classroom.teacher.id
            c2["course"]=classroom.course.id
            s1=[]
            for s2 in classroom.students:
                s1.append(s2.id)
            c2["students"]=s1
            c1.append(c2)
        data["Classrooms"]=c1

        with open ("data.json","wt") as f1:
            d1=json.dumps(data)
            f1.write(d1)

        if exit_check:
            exit()
        else:
            level="root"

    elif level=="student_select":
        s1=students[selected_student_index]
        menus=["1.info","2.add course","3.delet course","4.set scores","0.back"]
        for menu in menus :
            time.sleep(0.1)
            print(menu)
        cmd= get_int(">>")
        if cmd==1:
            print(s1)
            print("courses:")
            for course in s1.courses:
                print(f"{course}\t{course.score}")
        elif cmd==2:
            for course in courses:
                print(course)
            id=get_int("id: ")
            c1=Course(id,"",0)
            if c1 in courses:
                course_index=courses.index(c1)
                s1.courses.append(courses[course_index])
            else:
                print("not found")
        elif cmd==3:
            for course in s1.courses:
                print(course)
            id=get_int("id: ")
            c1=Course(id,"",0)
            if c1 in s1.courses:
                s1.courses.remove(c1)
            else:
                print("not found")
        elif cmd==4:
            for crs in s1.courses:
                if crs.score<10:
                    print(crs)
                    try:
                        score=float(input("score:"))
                    except ValueError:
                        print("Error: Invalid number entered")
                    else:
                        crs.score=score
        elif cmd==0:
            level="students"
    
    elif level=="teacher_select":
        t1=teachers[selected_teacher_index]
        print("1.info\n2.add course\n3.delet course\n0.back")
        cmd= get_int(">>")
        if cmd==1:
            print(t1)
            print("courses:")
            for course in t1.courses:
                print(course)
        elif cmd==2:
            for course in courses:
                print(course)
            id=get_int("id: ")
            c1=Course(id,"",0)
            if c1 in courses:
                course_index=courses.index(c1)
                t1.courses.append(courses[course_index])
            else:
                print("not found")
        elif cmd==3:
            for course in t1.courses:
                print(course)
            id=get_int("id: ")
            c1=Course(id,"",0)
            if c1 in t1.courses:
                t1.courses.remove(c1)
            else:
                print("not found")
        elif cmd==0:
            level="teachers"
    
    elif level=="select_classroom":
        classroom=classrooms[selected_classroom_index]
        print("1.view info\n2.chang course\n3.change teacher\n4.add student\n5.remove student\n0.back")
        cmd= get_int(">>")
        if cmd==1:
            print(f"id: {classroom.id}\nTeacher: {classroom.teacher}\ncourse: {classroom.course}\nStudents:")
            for s1 in classroom.students:
                print(s1)
        elif cmd==2:
            classroom=classrooms[selected_classroom_index]
            for c2 in courses:
                if c2!=classroom.course:
                    print(c2)
            id_course=get_int("id course: ")
            c1=Course(id_course,"",0)
            if c1 in courses:
                course=courses[courses.index(c1)]
                classroom.course=course
                if not(c1 in classroom.teacher.courses):
                    classroom.teacher=None
                stds=[]
                for s1 in classroom.students:
                    if c1 in s1.courses:
                        stds.append(s1)
                classroom.students=stds
            else:
                print("does not exist")
        elif cmd==3:
            for t1 in teachers:
                if classroom.course in t1.courses and (not(classroom.teacher) or classroom.teacher!=t1):
                    print(t1)
            id_teacher=get_int("id teacher: ")
            t1=Teacher(id_teacher,"","","")
            if t1 in teachers:
                teacher=teachers[teachers.index(t1)]
                classroom.teacher=teacher
            else:
                print("does not exist")
        elif cmd==4:
            for student in students:
                if not(student in classroom.students) and classroom.course in student.courses and student.courses[student.courses.index(classroom.course)].score<10:
                    print(student)
            id_student=get_int("id student: ")
            s1=Student(id_student,"","")
            if s1 in students:
                classroom.students.append(students[students.index(s1)])
            else:
                print("not found")
        elif cmd==5:
            for student in classroom.students:
                print(student)
            id_student=get_int("id student: ")
            s1=Student(id_student,"","")
            if s1 in classroom.students:
                classroom.students.remove(s1)
            else:
                print("not found")
        elif cmd==0:
            level="classrooms"
 
    elif level=="exit":
        print("Would you like to save your changes before exiting? (Y/n)")
        cmd=input(">>")
        if cmd == "y" or cmd=="Y":
            level="save"
            exit_check=True
        elif cmd=="n" or cmd=="N":
            exit()