# School/University managment system

This is a project for school/university managment system that let you manage studnets , teachers , courses and classrooms .
You can save and load data from data.json file .
You can add , edit or delete them but there are some rules here : You cannot edit or delete some methods for example; If a course rigested for a student , it cannot be removed that and...


This project is very useful and functional for manage school/university



## Structurs
- ### class:
  - #### Student:
     ##### properties of this class are id , name , family , and courses
  - #### Teacher:
     ##### properties of this class are id , name , family , grade , and courses
  - #### Course:
     ##### properties of this class are id , name , unites , and scores
  - #### Classroom:
     ##### properties of this class are id , name , course , teacher , and students



## Instruction
This programe has multiple menus , you can perform the related action or open each menu by entering the number corresponding to the desired option . These menus are categorized and desined to be very practical and simple , so everyone can use the application easily ; when you run the application , this menu opens:

```
1.students
2.teachers
3.courses
4.classrooms
5.save
0.exit
```
For example if you select `students` this menu will open , allowing you to add, edit, delete, or manage students, and more:

```
1.add student
2.edit student
3.delete student
4.view students
5.select student
0.back
```
If you select `select student` and enter the corresponding student ID this menu will open, allowing you to manage matters related to the student's courses and scores :

```
1.info
2.add course
3.delet course
4.set scores
0.back
```
You can open the other menues in the same way and use their features as well.
 
