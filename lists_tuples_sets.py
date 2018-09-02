my_variable = "hello"

grades = [77, 80, 90] #list -> can append to it and change contents
tuple_grades = (77, 80, 90) #tuple -> immutable 
							#you can add to it like add another tuple to it
							#but can't change its contents
							#ex: tuple += (100,) -> (77, 80, 90, 100)
set_grades = {77, 80, 90} #set -> unique & unordered
						  #you can /add/ things to a set

set_grades.add(60)
#print(set_grades)

##Set operations

your_lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}

print(your_lottery_numbers.union(winning_numbers)) 

#blah.union(blah2) = add blahs, no duplicates bc set
#blah.intersection(blah2) = add blahs
#blah.difference(blah2) = difference between blahs