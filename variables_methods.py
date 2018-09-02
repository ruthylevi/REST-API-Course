a = 5
b = 10
my_variable = 56

string_variable = 'hello'
double_quotes = "hello"

#print(my_variable)
#print(string_variable)

##

def my_print_method(my_argument):
	print(my_argument)

#my_print_method('eeeeEEEeee')

def my_multiply_method(number_one, number_two):
	return number_one * number_two

result = my_multiply_method(5,3)
#my_print_method(result)

my_print_method(my_multiply_method(5,3))