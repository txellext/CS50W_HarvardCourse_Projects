people = [
    {"name": "Harry", 
    "house": "Gryffindor"},
    {"name": "Cho", 
    "house": "Ravenclaw"},
    {"name": "Draco", 
    "house": "Slytherin"}
    }

# Define a functions that tells how to sort this array with objects
#def f(person):
 #   return person["name"]


#people.sort(key=f) 
# We include a funciton lambda as a single value in a single line. 
people.sort(key=lambda person: person["name"]) # lambda input: output

print(people)