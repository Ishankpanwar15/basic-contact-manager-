def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    
    person = {"name": name, "age": age, "email":email }
    return person

def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

def delete_contact(people):
    display_people(people)

    while True:
        number = input("Enter a number to delete: ")
        try: 
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number,  out of range. ")
            else:
                break
        except:
            print("Invalid number")


    people.pop(number - 1)
    print("person deleted")


def search_person(people):
    search_name = input("search for a name: ")
    result = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            result.append(person)


    display_people(result )  

def list_persons(people):
    if len(people) == 0:
        print("first you have to feed some contacts")
    
    
    display_people(people)

print("Hii, welcome to the Contact Management System.")
print("first you have to feed some data:")
print()
people = []
while True:
    command = input("you can 'Add', 'Delete' , 'search' or 'list' and 'Q' for quit: ").lower( )
    if command == "add":
        person = add_person()
        people.append(person)
        display_people(people)
        print("person added")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":    
        search_person(people)
    elif command == "list":
        list_persons(people)
    elif command == "q":
        break
    else:
        print("invalid input")
 
 
 
