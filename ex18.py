# Example code showing how to define a dictionary and add a new key/value pair to it
person = {'name': 'Bob', 'dob': '12/03/1975', 'gender':'male'}
person['height'] = 74
print(person)

# Example code showing how to iterate over the keys and values in a dictionary
for key in person:
    print(key, ":", person[key])
print('-'*20)
# >>>>>>>>>>  END OF EXAMPLES <<<<<<<<<<<<
me = {'Name' : 'Zachary', 'Dob': '11/17/2002', 'Gender': 'Male', 'Eye Color': 'Brown'}
me['Height'] = 74
# Write your solution for Exercises 1 and 2 below here:
# Write your solution for Exercise 3 below here:
me['Middle Name'] = 'Jacob'
me['Surname'] = 'Turner'
# Write your solution for Exercise 4 below here:
me['Shoe Size'] = 11
# Write your solution for Exercise 5 below here:
del me['Eye Color']
for key in me:
  print(key, ":", me[key])

