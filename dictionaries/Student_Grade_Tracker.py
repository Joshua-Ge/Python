students = {
    "John" : 34,
    "Jim" : 45,
    "Jill" : 56,
    "Max" : 67,
    "Tim" : 78,
    "Ron" : 89
}



def add_student(dictionary:object):
    dic = dictionary
    student = input("What is the name of the student you'd like to add? >> ")
    grade = input(f"What is the grade of {student}? >> ")
    grade = int(grade)
    dic[student] = grade

def remove_student(dictionary:object):
    dic = dictionary
    student = input("Which student would you like to remove? >> ")
    dic.pop(student)

def print_students(dictionary:object):
    dic = dictionary
    print(dic)

def average_grade(dictionary:object):
    humans = 0
    total = 0
    dic = dictionary
    total = 0
    for student ,grade in dic.items():
        humans += 1
        total += grade

    average = total / humans
    average = round(average, 2)

    print(f"The average grade was: {average}")

using = True

while using == True:
    action = input("What would you like to do? >> ")
    
    if action == "quit":
        using = False
    elif action == "show":
        print_students(students)
    elif action == "add":
        add_student(students)
    elif action == "remove":
        remove_student(students)
    elif action == "average":
        average_grade(students)
    else:
        print("Please enter a valid response (quit, show, add, remove, average)")



