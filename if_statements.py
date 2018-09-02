# should_continue = True
# if should_continue:
# 	print("Hello")

# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")

# if person in known_people:
# 	print("You know {}!".format(person))
# else:
# 	print("You don't know {}!".format(person))

def who_do_you_know():
	#ask the user for a list of people they know
	#split the string into a list
	#return that list

	people = input("Give me a list of people you know, separated by a comma: ")
	return [person.strip() for person in people.split(",")]

	
def ask_user():
	#ask user for a name
	#see if their name is in the list of people they know 
	#print out that they know the person

	name = input("Give me a name: ")
	if name in who_do_you_know():
		print("You know {}!".format(name))
	else:
		print("You don't know {}!".format(name))

ask_user()