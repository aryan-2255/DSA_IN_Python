d = {}
print(type(d),d)
 
# method 1 to create a dictionary
d = {
    "name": "aryan",
    "age" : "25",
    "school": "polaris"
    }
print(d)

# method 2 to create a dictionary
d2 = dict(name= "aryan" , age = 25 , school = "polaris")
print(d2)

# method 3 to create a dictionary
d3 = {}
d3["name"] = "aryan"
d3["age"] = 25
d3["school"] = "polaris"
print(d3)

# retereving values from dictionary: name_of_dictionary[key]
print(d3["name"])
print(d3["age"])
print(d3["school"])

# check particular key exist in dictionar: using (in operator)
print("age" in d3)
print("Name" in d3)   # you think name is in dictionary but see carefully here N is capital and the key in    lower case so you change the key that's why it result false

# keys()
print(d3.keys())
for key in d3.keys():
    print(key)
# values()
print(d3.values())
# items()
print(d3.items())


## important: update a dictionary

# Initial dictionary
my_dict = {'name': 'Alice', 'age': 25}

# Updating the value of 'age'
my_dict['age'] = 30  # Changing age from 25 to 30

print(my_dict)  # Output: {'name': 'Alice', 'age': 30}

# update method in dictionary
d3.update({'balance':0, 'location':'haryana'})
print(d3)

# Nested Dictionaries:
d4 = {'description':{'name':'rahul','age': 21, 'school':'polaris'}}
print(d4)
print(d4['description'])
print(d4['description']['name'])
print(d4['description']['age'])
print(d4['description']['school'])
# modifing nested dictionary
d4['description']['age'] = 25
print(d4['description']['age'])

#
