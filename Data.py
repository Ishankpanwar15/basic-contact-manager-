def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    
    person = {"name": name, "age": age, "email":email }
    return person

def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])
        

print("Hii, welcome to the Contact Management System.")
print("first you have to feed some data:")
print()
people = []
while True:
    command = input("you can 'Add':").lower( )

    if command == "add":
        person = add_person()
        people.append(person)
        display_people(people)
        print("person added")
    else:
        print("invalid input")
 
 
 
