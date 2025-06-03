phoneNumbers = {

}

def add_number(dic:object):
    name = input("Who does this number belong to? >> ")
    number = input("What is the phone number? >> ")
    name = name.lower().strip()
    number.strip()
    dic[name] = number

def remove_number(dic:object):
    method = input("How would you like to remove the number? (num, name) >> ")
    method = method.strip().lower()
    if method == "num":
        number = input("What is the number? >> ")
        dic.pop(number)
    elif method == "name":
        name = input("What is the name of the person with the number? (lowercase) >> ")
        dic.pop(name)
    else:
        print("Please enter a valid option")

def show_number(dic:object):
    print(dic.values())

def search_number(dic:object):
    response = ""
    method = input("How will you search? (name, num) >> ")
    method = method.strip().lower()
    if method == "name":
        name = input("What is the name you are looking for? (Lowercase) >> ")
        for k,v in dic.items():
            if k == name:
                response = [k,v]
    elif method == "num":
        number = input("What is the number of the perosn you are looking for? >> ")
        for k,v in dic.items():
            if v == number:
                response = [k,v]
    else:
        print("Please select a valid answer")
    
    print(response)

    
using = True

while using == True:
    action = input("What will you do? >> ")

    if action == "quit":
        using  = False
    elif action == "add":
        add_number(phoneNumbers)
    elif action == "remove":
        remove_number(phoneNumbers)
    elif action == "show":
        show_number(phoneNumbers)
    else:
        print("Please enter a valid response")
