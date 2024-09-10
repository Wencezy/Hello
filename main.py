# print("Hello World")

# message ="Hello world"
# num =20
# ifPassed = True

# print(message)

# name = "Wence"
# message = "Hello"
# # mng = name+message
# mng= "{}{} how are you".format(name, message)
# print(mng)

# num =input("Enter first number")
# num2=input("Emter second number")

# if num==num2:
#     print("true")
# else:
#     print("false")    

# num1= 30
# num =input("Enter first number")
# num2=input("Emter second number")
# total= int(num) + int(num2)
# print(total)

# if total < 30:
#     print("the total is{total} less than 30")
#  elif total=30:
#     print("the total is{total}  equal to 30")
# elif total > 30:
#     print("the total is{total} greater than 30")         
# else:
#     print("The number can not be added")

# def greetings(name):
#     print("good morning {}".format(name))
    
# greetings("Wence")  

# def addNumber(num1, num2):
#     return num1 + num2
# print(addNumber(30, 40) )
   

#    def addNumber(num1, num2, num3):
#     average=(num1 + num2+   num3)/3
#     return average >=10
#     print(addNumber(8, 12, 9)) # output:
#         False 
#     print(addNumber(10, 12, 9)) # output:
#       True 

# def checkAverage(note1, note2, note3):
#     total = int(note1) + int(note2) + int(note3)
#     average = total / 3
#     print(f"Your average is: {float(average):.2F}")
#     if average > 10:
#         print("You have passed")
#     elif average == 10:
#         print("You had the average")
#     else:
#         print("You failed") 

# note1 =int( input("Enter note1:"))
# note2 = int(input("Enter note2:"))
# note3 = int(input("Enter note3:") )
# checkAverage(note1, note2, note3)  

# class Student:
#     def init(self,name):
#         self.name= name
#         self.marks=[]

#     def add_marks(self):
#             for i in range(3):
#                 marks = float(input(f"Enter mark {i+1} for {self.name}:"))
#                 self.marks.append(mark)

#     def calculate_average(self):
#         return sum(self.marks)/len(self.marks)

# def main():
#     Student = []
#     for j in range(5):
#         name = input(f"Enter name of student {j+1}:")
#         student = Student(name)
#         student.add_marks()
#         students.append(student)

#     passed_students = [student.name for student in students if
#     student.calculate_average()>=10]

#     print("Students who passed:")
#     for name in passed_students:
#         print(name)

# if "name" == "main":
#     main()      

# students = []
# def get_student_name():
#     return input("Enter student name:")

# def get_marks():
#     marks= []
#     for i in range(3):
#         mark = float(input(f"Enter mark {i+1}:"))
#         marks.append(mark)
#     return marks

# def calculate_average(marks):
#     return sum(marks) / len(marks)

# def print_student_result(name, average):
#     if average >=10:
#         print(f"{name} passed with average {average:.2f}")
#     else:
#         print(f"{name} failed with average {average:.2f}")

# def main():
#     for i in range(5):
#         name = get_student_name()
#         marks = get_marks()
#         average = calculate_average(marks)
#         print_student_result(name, average)

# main()




students = []
for i in range(5):
    name = input(f"Enter students {i+1} name:")
    mark1 = float(input("Enter mark1:"))
    mark2 = float(input("Enter mark2:"))
    mark3 = float(input("Enter mark3:"))

    total = mark1 + mark2 + mark3
    average = total/3
    print(f"{'name'} average is {float(average)}:.2f")

    student = {
        'name':name,
        'marks':{
            'mark1':mark1,
            'mark2':mark2,
            'mark3':mark3,
        }
    }

    if average >=10:
        students.append(student)

for stud in students:
    print(stud['name'])

# we use django for webapps ,its a python frame work and it can be use to do the whole projrct or just the backend
# its the backend that makes the side dynamic , its the part that the user does not see it is the logic behind the page