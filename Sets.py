numbers={1.5,"Ronav",3}
print(numbers)

names = {"Ronav","George","Josh"}
print(names)

mixed_set = {"Hello",110,-2,"bye"}
print(mixed_set)

empty_set1 = {}     # this line will create an empty dictionary

# to create an empty set
empty_set2 = set()

print(type(empty_set1))
print(type(empty_set2))

num1 = 2
num2 = 1.5
name = "Ronav"
value = True

print(type(num1))
print(type(num2))
print(type(name))
print(type(value))

duplicate_set = {1,2,3,4,5,1}
print(duplicate_set)

duplicate_set.add(1000)
print(duplicate_set)

companies = {'Amazon', 'info'}
tech_companies = ['apple', 'google', 'apple']

# using update() method
companies.update(tech_companies)

print(companies)

# Output: {'google', 'apple', 'Amazon', 'info'}

companies.discard("info")
print(companies)